from repository import company_repository
from app import redis_cache

def createCompany(requestCompanies, requestTags):
    # Company 저장
    savedCompany = company_repository.createCompany();
    id = savedCompany.id

    # CompanyName 저장
    for company in requestCompanies:

        type = company
        name = requestCompanies[company]

        # redis에 key(회사 이름), value(언어) 추가
        redis_cache.set(name, type)

        # db에 저장
        company_repository.createCompanyName(id, type, name)

    # TagName 저장
    for tag in requestTags:
        for item in tag:
            for t in tag[item]:
                type = t;
                name = tag[item][t]
                company_repository.createTagName(id, type, name)

    return id