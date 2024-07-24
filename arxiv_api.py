import arxiv
from datetime import datetime
import json

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

# 결과를 저장할 리스트
papers = []
papers_with_journal = []

# 논문 ID 초기화
paper_id = 1

# 결과를 JSON 형태로 저장
for result in results:
    paper_info = {
        "id": paper_id,
        "title": result.title,
        "authors": [author.name for author in result.authors],
        "published": result.published.strftime("%Y-%m-%d"),
        "summary": result.summary,
        "journal_ref": result.journal_ref if result.journal_ref else 'N/A'
    }
    papers.append(paper_info)

    if result.journal_ref:
        papers_with_journal.append(paper_info)

    paper_id += 1

# 파일 이름 생성
file_name_all = f"arxiv_papers_{start_date.strftime('%Y%m%d')}_to_{end_date.strftime('%Y%m%d')}.json"
file_name_journal = f"arxiv_papers_with_journal_{start_date.strftime('%Y%m%d')}_to_{end_date.strftime('%Y%m%d')}.json"

# JSON 파일로 저장
with open(file_name_all, 'w', encoding='utf-8') as f:
    json.dump(papers, f, indent=4, ensure_ascii=False)

with open(file_name_journal, 'w', encoding='utf-8') as f:
    json.dump(papers_with_journal, f, indent=4, ensure_ascii=False)

print(f"Results saved to {file_name_all}")
print(f"Results with journal references saved to {file_name_journal}")