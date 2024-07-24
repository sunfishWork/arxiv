import arxiv
from datetime import datetime

# 날짜 범위 설정
start_date = datetime(2024, 7, 16)
end_date = datetime(2024, 7, 23)

# 카테고리 및 날짜 범위 설정
category = "cs.IT OR cs.NI OR eess.SP OR eess.IV OR eess.SY"
query = f"cat:{category} AND submittedDate:[20240716 TO 20240723]"

# API 클라이언트 생성
client = arxiv.Client()

# 검색 조건 설정
search = arxiv.Search(
    query=query,
    sort_by=arxiv.SortCriterion.SubmittedDate
)

# 결과 가져오기
results = client.results(search)

# 결과 출력
for result in results:
    print(f"Title: {result.title}")
    print(f"Authors: {', '.join([author.name for author in result.authors])}")
    print(f"Published: {result.published}")
    print(f"Summary: {result.summary}")
    print(f"Journal Reference: {result.journal_ref if result.journal_ref else 'N/A'}")
    print("-" * 80)