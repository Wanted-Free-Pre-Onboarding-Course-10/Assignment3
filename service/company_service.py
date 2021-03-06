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
        if name == '':
            continue

        redis_cache.sadd(name, type)

        # db에 저장
        company_repository.createCompanyName(id, type, name)

    # TagName 저장
    for tag in requestTags:
        for item in tag:
            for t in tag[item]:
                type = t
                name = tag[item][t]
                if name == '':
                    continue
                findTagName = company_repository.findTagNameByNameAndType(name, type);
                tagId = 1;
                print("findTagAme : ")
                print(name + ", " + type )
                print(findTagName)

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


def getOneCompany(companyName, language):

    companyNameResult = company_repository.getOneCompanyByCompanyName(companyName)

    if len(companyNameResult) == 0:
        abort(404, '찾는 회사가 없습니다.')

    resultArray = []
    duplicate = []

    for queryResult in companyNameResult:
        companyId = queryResult.Company.id
        if companyId in duplicate: continue
        duplicate.append(companyId)
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

def findCompanyNameAndTagsByLanguage(id, language):
    companyName = company_repository.getOneCompanyByCompanyIdAndLanguageType(id, language)
    name = companyName.name

    print("service company name : " + name)

    tagResult = company_repository.getTagsByCompanyIdAndTagName(id, language)

    tags = []

    print("service tagResult")
    print(tagResult)


    for tag in tagResult:
        tags.append(tag.name)

    result = {
        "company_name": name,
        "tags": tags
    }

    return result