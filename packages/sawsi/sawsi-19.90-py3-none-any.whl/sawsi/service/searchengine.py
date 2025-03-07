
"""
검색엔진 개발 예시
"""
import regex
from sawsi.aws.dynamodb.api import DynamoDBAPI
from typing import Optional
from collections import Counter
from decimal import Decimal


class SearchEngine:
    def __init__(self, dynamo_db_api: DynamoDBAPI, table_name: str):
        self.table_name = table_name
        self.dynamo_db_api = dynamo_db_api

    def init_table(self):
        response = self.dynamo_db_api.create_table(
            self.table_name,
            partition_key='i',
            partition_key_type='S',
            sort_key='p',
            sort_key_type='N'
        )
        print('response:', response)
        self._create_gsi()
        return response

    def _create_gsi(self):
        response = self.dynamo_db_api.create_global_index(
            self.table_name,
            partition_key='g',
            partition_key_type='S',
            sort_key='s',
            sort_key_type='N',
        )
        return response

    @classmethod
    def _make_n_gram(cls, text: str, n: int = 2) -> list[str]:
        """
        문자열을 받아 n-gram 리스트를 반환하는 함수
        :param text: 입력 문자열
        :param n: n-gram의 n 값 (기본값: 2)
        :return: n-gram 리스트
        """
        if n < 1:
            raise ValueError("n은 1 이상의 정수여야 합니다.")
        return [text[i:i + n] for i in range(len(text) - n + 1)]

    @classmethod
    def _pre_process(cls, value: str) -> str:
        """
        특수문자 및 이모지를 제거하고, 앞에 ^ 부착
        :param value: 입력 문자열
        :return: 전처리된 문자열
        """
        v = regex.sub(r'[^\p{L}\p{N}]', '', value)  # 문자(Letter) 및 숫자(Number)만 남김
        v = f'^{v}$'  # 앞에 ^ 부착
        return v

    def put_data(self, item_id: str, text: str):
        """
        레코드에 특정 필드의 text 에 대해 삽입
        field_value에서 특수문자 다 삭제하고 앞에 ^를 붙여서 한글자 검색 가능하게 변경
        :param item_id:
        :param text:
        :return:
        """
        v = self._pre_process(text)
        v_size = len(v)
        last_p = 0
        for idx, gram in enumerate(self._make_n_gram(v, 2)):
            self.dynamo_db_api.put_item(self.table_name, {
                'g': gram,  # 토큰
                'i': item_id,  # 가리키는 Item ID
                's': v_size,  # 총 문자열 사이즈
                'p': idx,  # 이 토큰의 gram 위치
            })
            last_p = idx
        # 입력된 총 문자열 사이즈보다 큰 것들은 다 삭제
        item_deleted = self.dynamo_db_api.delete_item_by_key(
            self.table_name,
            {
                'i': item_id,
                'p': last_p + 1
            }
        )
        item_deleted = item_deleted.get('Attributes', {})
        # print('first-item_deleted:', item_deleted)
        if item_deleted:  # 있으면, v_size 를 구해서 그만큼 삭제
            old_size = item_deleted['s']
            old_size = int(old_size)
            for idx in range(last_p + 2, old_size):
                item_deleted = self.dynamo_db_api.delete_item_by_key(
                    self.table_name,
                    {
                        'i': item_id,
                        'p': idx,
                    }
                )
                item_deleted = item_deleted.get('Attributes', {})
                # print('item_deleted:', item_deleted)

    def delete_data(self, item_id: str):
        """
        특정 Item 에 대해 검색 레코드 삭제
        :param item_id:
        :return:
        """
        # 일단 첫 토큰 삭제
        item_deleted = self.dynamo_db_api.delete_item_by_key(
            self.table_name,
            {
                'i': item_id,
                'p': 0,
            }
        )
        item_deleted = item_deleted.get('Attributes', {})
        # print('first-item_deleted:', item_deleted)
        if item_deleted:  # 있으면, v_size 를 구해서 그만큼 삭제
            old_size = item_deleted['s']
            old_size = int(old_size)
            for idx in range(1, old_size):
                item_deleted = self.dynamo_db_api.delete_item_by_key(
                    self.table_name,
                    {
                        'i': item_id,
                        'p': idx,
                    }
                )
                item_deleted = item_deleted.get('Attributes', {})
                # print('item_deleted:', item_deleted)


    @staticmethod
    def _convert_decimal(obj):
        """
        객체 내의 Decimal 타입을 int/float 등 JSON 직렬화 가능한 타입으로 변환.
        """
        if isinstance(obj, list):
            return [SearchEngine._convert_decimal(i) for i in obj]
        elif isinstance(obj, dict):
            return {k: SearchEngine._convert_decimal(v) for k, v in obj.items()}
        elif isinstance(obj, Decimal):
            # 정수인지 여부에 따라 int 또는 float로 변환
            return int(obj) if obj % 1 == 0 else float(obj)
        else:
            return obj

    def search(self, keyword: str, start_key: Optional[dict], limit: int = 10) -> tuple[list[str], Optional[dict]]:
        """
        n-gram 기반 검색을 수행합니다.
        검색어를 전처리한 후 n-gram(기본 2-gram) 리스트를 생성하고,
        각 n-gram에 대해 DynamoDB에서 항목들을 조회하여,
        item_id별로 '매칭 횟수', '전체 문자열 길이(s)', '토큰의 위치(p)'를 집계합니다.
        이후, 매칭 횟수가 높고(s가 검색어 길이에 가까우며, p 값이 낮은) 항목이 우선되도록 정렬합니다.

        또한, 각 n-gram 조회 결과에 대한 end_key를 별도로 관리하여 pagination을 지원합니다.

        :param keyword: 검색 키워드
        :param start_key: 페이지네이션을 위한 시작 키.
                          n-gram별로 {'gram_token': exclusive_start_key, ...} 형태로 전달됨.
        :return: (정렬된 item_id 리스트, 다음 페이지 조회를 위한 end_key 딕셔너리 또는 None)
        """
        # 1. 검색어 전처리 및 n-gram 생성
        processed_value = self._pre_process(keyword)
        v_size = len(processed_value)
        # n-gram 리스트(기본 n=2)와 각 n-gram의 빈도 계산 (검색어 내 중복 고려)
        query_grams = self._make_n_gram(processed_value, 2)
        gram_freq = Counter(query_grams)

        # 2. 각 유니크 n-gram에 대해 DynamoDB 조회 및 결과 집계
        # aggregated_results: { item_id: {'match_count': int, 'total_length': s, 'positions': [p, ...]} }
        aggregated_results: dict[str, dict] = {}
        # result_end_keys: n-gram별로 다음 조회를 위한 end_key 저장
        result_end_keys: dict[str, dict] = {}

        for gram in gram_freq:
            # start_key가 n-gram별로 전달되었다고 가정 (없으면 None)
            gram_start_key = start_key.get(gram) if start_key and gram in start_key else None

            # DynamoDB에서 해당 gram으로 조회
            items, gram_end_key = self.dynamo_db_api.query_items(
                table_name=self.table_name,
                pk_field='g',
                pk_value=gram,
                sk_condition='gte',
                sk_field='s',
                sk_value=v_size,
                reverse=False,
                limit=limit,
                consistent_read=False,
                start_key=gram_start_key  # pagination 지원 파라미터
            )
            # 만약 더 조회할 항목이 있다면, end_key를 저장
            if gram_end_key is not None:
                result_end_keys[gram] = gram_end_key

            # 조회된 각 항목에 대해 집계: n-gram의 빈도(gram_freq[gram])를 가중치로 적용
            for item in items:
                item_id = item["i"]
                # item['s']는 해당 아이템의 전체 문자열 길이 (검색어 삽입 시 기록한 값)
                # item['p']는 이 gram의 위치
                if item_id not in aggregated_results:
                    aggregated_results[item_id] = {
                        "match_count": 0,
                        "total_length": item["s"],
                        "positions": []
                    }
                # 검색어 내에서 gram이 여러 번 등장했다면 그만큼 가중치를 더함
                aggregated_results[item_id]["match_count"] += gram_freq[gram]
                aggregated_results[item_id]["positions"].append(item["p"])

        # 3. item_id별로 평균 위치 계산 등 추가 점수를 산출한 후, 정렬 기준 마련
        # 정렬 기준: (1) 매칭 횟수는 많을수록 좋음, (2) 전체 문자열 길이(s)는 검색어 길이(v_size)에 가까울수록 좋음,
        # (3) 위치(p)는 낮을수록(앞쪽에 있을수록) 좋은 것으로 간주
        scored_items = []
        for item_id, data in aggregated_results.items():
            match_count = data["match_count"]
            total_length = data["total_length"]
            avg_position = sum(data["positions"]) / len(data["positions"]) if data["positions"] else 0
            # 정렬을 위한 튜플: 매칭 횟수 내림차순, total_length 오름차순, avg_position 오름차순
            scored_items.append((item_id, match_count, total_length, avg_position))

        scored_items.sort(key=lambda x: (-x[1], x[2], x[3]))
        result_item_ids = [item[0] for item in scored_items]

        # 4. Pagination: 하나라도 n-gram 조회에 end_key가 있으면 반환 딕셔너리에 포함
        result_end_key = result_end_keys if result_end_keys else None
        # 여기서 end_key 내 Decimal 타입을 일반 타입으로 변환
        result_end_key = SearchEngine._convert_decimal(result_end_key) if result_end_key is not None else None

        return result_item_ids, result_end_key


if __name__ == '__main__':
    import api

    se = SearchEngine(api.dynamo, 'search-n-gram')

    print("=== 테이블 초기화 ===")
    se.init_table()

    # 1. 테스트 데이터 리스트 (아이템 ID, 텍스트)
    test_data = [
        ("TEST1", "신선한 감자와 고소한 은행"),
        ("TEST2", "감자튀김과 바삭한 감자"),
        ("TEST3", "따끈한 감자탕과 매콤한 국물"),
        ("TEST4", "은행나무 아래서 책 읽기"),
        ("TEST5", "감자와 은행 그리고 사과"),
        ("TEST6", "고소한 두부와 신선한 야채"),
        ("TEST7", "감미로운 음악과 감동적인 영화"),
        ("TEST8", "감기 걸린 감자, 감정이 북받쳐"),
        ("TEST9", "매운 고추로 만든 감기약"),
        ("TEST10", "맛있는 감자전과 김치전"),
        ("TEST11", "은행나무 가로수 길을 걸으며 감미로운 노래"),
        ("TEST12", "고소한 견과류와 함께 먹는 감자칩"),
        ("TEST13", "따뜻한 사과차와 함께하는 감성적인 시간"),
        ("TEST14", "새콤달콤한 감귤과 신선한 과일"),
        ("TEST15", "매운 청양고추와 감칠맛 나는 요리"),
        ("TEST16", "은행에서 대출을 받는 방법"),
        ("TEST17", "감미로운 와인과 함께하는 저녁"),
        ("TEST18", "감동적인 영화와 눈물나는 감정"),
        ("TEST19", "소금과 후추로 간을 맞춘 감자요리"),
        ("TEST20", "바삭한 감자튀김과 매콤한 소스"),
    ]

    # 2. Pagination 테스트를 위한 더미 데이터 개수
    dummy_data_count = 120
    dummy_text = "감자"

    print("\n=== 테스트 데이터 삽입 ===")
    for item_id, text in test_data:
        se.put_data(item_id, text)

    print(f"\n=== Pagination 테스트: DUMMY 데이터 삽입 ({dummy_data_count}개) ===")
    for i in range(dummy_data_count):
        se.put_data(f"DUMMY{i}", dummy_text)

    # 3. 검색어 리스트
    test_queries = ["감", "감자", "은행", "사과", "고추", "감미로운", "고소한", "감동", '사과차와 감성적인']


    # 4. 검색 결과 출력 함수
    def print_search_results(query, first_results, first_end_key):
        print("\n------------------------------")
        print(f"🔍 Search Query: '{query}'")
        print(f"✅ 검색 결과 (유사도 순, 최대 100개): {first_results}")
        print(f"📌 Pagination 정보: {first_end_key}")

        # end_key가 있다면 추가 페이지 조회 테스트
        if first_end_key:
            next_results, next_end_key = se.search(query, first_end_key)
            print(f"🔄 Next Page 검색 결과 (유사도 순, 최대 100개): {next_results}")
            print(f"📌 Next Page Pagination 정보: {next_end_key}")


    print("\n=== 검색 테스트 ===")
    for query in test_queries:
        first_results, first_end_key = se.search(query, None)
        print_search_results(query, first_results, first_end_key)
