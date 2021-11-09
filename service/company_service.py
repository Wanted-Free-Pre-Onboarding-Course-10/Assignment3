from sqlalchemy import and_

from model.models import Company
from model.models import CompanyName
from model.models import TagName
from model.models import CompanyTagName
from repository import company_repository
from app import redis_cache
from app import db
from flask import abort


def createCompany(requestCompanies, requestTags):
    # Company 저장
    savedCompany = company_repository.createCompany();
    id = savedCompany.id

    # CompanyName 저장
    for company in requestCompanies:
        type = company
        name = requestCompanies[company]

        redis_cache.sadd(name, type)

        # db에 저장
        company_repository.createCompanyName(id, type, name)

    # TagName 저장
    for tag in requestTags:
        for item in tag:
            for t in tag[item]:
                type = t
                name = tag[item][t]
                company_repository.createTagName(id, type, name)

    return id

def getOneCompany(query, language):

    companyNameResult = company_repository.getOneCompanyByCompanyName(query)

    if len(companyNameResult) == 0:
        abort(404, '찾는 회사가 없습니다.')

    resultArray = []

    for queryResult in companyNameResult:
        companyId = queryResult.Company.id
        company = company_repository.getOneCompanyByCompanyIdAndLanguageType(companyId, language)

        tagResult = company_repository.getTagsByCompanyIdAndTagName(companyId, language)

        tags = []

        for tag in tagResult:
            tags.append(tag.name)


        result = {
            "company_name": company.name,
            "tags": tags
        }

        resultArray.append(result)

    return resultArray

