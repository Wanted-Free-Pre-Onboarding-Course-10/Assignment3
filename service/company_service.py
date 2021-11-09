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
                findTagName = company_repository.findTagNameByNameAndType(name, type);
                tagId = 1;

                if findTagName == None:
                    # 해당 이름과 타입의 태그이름이 태그 테이블에 없으면
                    tagId = company_repository.createTagName(type, name).id
                else:
                    # 해당 이름의 태그이름이 있으면
                    tagId = findTagName.id

                # CompanyTagName 저장
                company_repository.createCompanyTagName(id, tagId)

    # Company id 리턴
    return id


def getOneCompany(query, language):
    if query == '':
        abort(404, '잘못된 요청입니다.')

    companyNameResult = company_repository.getOneCompanyByCompanyName(query)

    if len(companyNameResult) == 0:
        abort(404, '찾는 회사가 없습니다.')

    resultArray = []

    for queryResult in companyNameResult:
        companyId = queryResult.Company.id
        print(companyId)
        company = company_repository.getOneCompanyByCompanyIdAndLanguageType(companyId, language)

        tagResult = company_repository.getTagsByCompanyIdAndTagName(companyId, language)

        tags = []

        idx = 0
        for tag in tagResult:
            tags.append({f"tag{idx}": tag.name})

        result = {
            "company_name": company.name,
            "tags": tags
        }

        resultArray.append(result)

    return resultArray