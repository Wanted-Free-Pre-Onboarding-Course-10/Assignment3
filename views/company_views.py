import json

from flask import Blueprint, make_response, jsonify, request
import pprint
from service import company_service


pp = pprint.PrettyPrinter(indent=4)
bp = Blueprint('companies', __name__, url_prefix='/companies')

@bp.route('/', methods=["POST"])
def createCompanies():
    result = request.get_json()
    requestCompanies = result['company_name'];

    requestTags = result['tags'];

    # savedId : Company id
    savedId = company_service.createCompany(requestCompanies, requestTags)

    # 요청헤더에 담긴 언어 조회 - language에 맞는
    language = request.headers.get('x-wanted-language')

    result = company_service.findCompanyNameAndTagsByLanguage(savedId, language)

    return jsonify(result)


@bp.route('/<companyName>', methods=['GET'])
def companies(companyName):

    language = request.headers.get('x-wanted-language')
    response = company_service.getOneCompany(companyName, language)

    print(response)

    return jsonify(response)

@bp.route('/test', methods=['POST'])
def test():
    request = [{"company_name":{"ko":"company_ko","en":"company_en","ja":"company_ja"},"tags":[{"tag_name":{"ko":"tag_ko","en":"tag_en","ja":"tag_ja"}}]},{"company_name":{"ko":"원티드랩","en":"Wantedlab","ja":""},"tags":[{"tag_name":{"ko":"태그_4|태그_20|태그_16","en":"tag_4|tag_20|tag_16","ja":"タグ_4|タグ_20|タグ_16"}}]},{"company_name":{"ko":"","en":"OKAY.com","ja":""},"tags":[{"tag_name":{"ko":"태그_24|태그_27|태그_4","en":"tag_24|tag_27|tag_4","ja":"タグ_24|タグ_27|タグ_4"}}]},{"company_name":{"ko":"이상한마케팅","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_25|태그_6|태그_14|태그_9","en":"tag_25|tag_6|tag_14|tag_9","ja":"タグ_25|タグ_6|タグ_14|タグ_9"}}]},{"company_name":{"ko":"인포뱅크","en":"infobank","ja":""},"tags":[{"tag_name":{"ko":"태그_25","en":"tag_25","ja":"タグ_25"}}]},{"company_name":{"ko":"아이씨그룹","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_1|태그_23|태그_28|태그_14","en":"tag_1|tag_23|tag_28|tag_14","ja":"タグ_1|タグ_23|タグ_28|タグ_14"}}]},{"company_name":{"ko":"딤딤섬 대구점","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_22|태그_29|태그_2|태그_13","en":"tag_22|tag_29|tag_2|tag_13","ja":"タグ_22|タグ_29|タグ_2|タグ_13"}}]},{"company_name":{"ko":"파운데이션엑스","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_8","en":"tag_8","ja":"タグ_8"}}]},{"company_name":{"ko":"엣지랭크","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_5|태그_11|태그_26|태그_1","en":"tag_5|tag_11|tag_26|tag_1","ja":"タグ_5|タグ_11|タグ_26|タグ_1"}}]},{"company_name":{"ko":"커넥티어","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_11|태그_21","en":"tag_11|tag_21","ja":"タグ_11|タグ_21"}}]},{"company_name":{"ko":"자버(Jober)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_2|태그_16","en":"tag_2|tag_16","ja":"タグ_2|タグ_16"}}]},{"company_name":{"ko":"앨리스헬스케어","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_13|태그_5|태그_12","en":"tag_13|tag_5|tag_12","ja":"タグ_13|タグ_5|タグ_12"}}]},{"company_name":{"ko":"(주)몬스터스튜디오","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_19","en":"tag_19","ja":"タグ_19"}}]},{"company_name":{"ko":"SM Entertainment Japan","en":"","ja":"株式会社SM Entertainment Japan"},"tags":[{"tag_name":{"ko":"태그_23|태그_11|태그_15","en":"tag_23|tag_11|tag_15","ja":"タグ_23|タグ_11|タグ_15"}}]},{"company_name":{"ko":"쿠차","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_27|태그_5|태그_26","en":"tag_27|tag_5|tag_26","ja":"タグ_27|タグ_5|タグ_26"}}]},{"company_name":{"ko":"ZMP","en":"","ja":"株式会社ZMP"},"tags":[{"tag_name":{"ko":"태그_10|태그_2|태그_21|태그_24","en":"tag_10|tag_2|tag_21|tag_24","ja":"タグ_10|タグ_2|タグ_21|タグ_24"}}]},{"company_name":{"ko":"몽키랩","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_7|태그_23|태그_28","en":"tag_7|tag_23|tag_28","ja":"タグ_7|タグ_23|タグ_28"}}]},{"company_name":{"ko":"와이케이비앤씨","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_14|태그_29|태그_6","en":"tag_14|tag_29|tag_6","ja":"タグ_14|タグ_29|タグ_6"}}]},{"company_name":{"ko":"코츠테크놀로지","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_12|태그_2","en":"tag_12|tag_2","ja":"タグ_12|タグ_2"}}]},{"company_name":{"ko":"비고라이브","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_13|태그_19","en":"tag_13|tag_19","ja":"タグ_13|タグ_19"}}]},{"company_name":{"ko":"크로싱","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_21|태그_30|태그_12|태그_28","en":"tag_21|tag_30|tag_12|tag_28","ja":"タグ_21|タグ_30|タグ_12|タグ_28"}}]},{"company_name":{"ko":"트리노드","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_7|태그_19|태그_12|태그_17","en":"tag_7|tag_19|tag_12|tag_17","ja":"タグ_7|タグ_19|タグ_12|タグ_17"}}]},{"company_name":{"ko":"와이즈키즈(wisekids)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_1|태그_9|태그_17|태그_14","en":"tag_1|tag_9|tag_17|tag_14","ja":"タグ_1|タグ_9|タグ_17|タグ_14"}}]},{"company_name":{"ko":"Obelab","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_6","en":"tag_6","ja":"タグ_6"}}]},{"company_name":{"ko":"","en":"Foodpanda","ja":""},"tags":[{"tag_name":{"ko":"태그_26","en":"tag_26","ja":"タグ_26"}}]},{"company_name":{"ko":"웹티즌","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_28|태그_25|태그_7|태그_13","en":"tag_28|tag_25|tag_7|tag_13","ja":"タグ_28|タグ_25|タグ_7|タグ_13"}}]},{"company_name":{"ko":"마이셀럽스","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_2|태그_8|태그_22|태그_27","en":"tag_2|tag_8|tag_22|tag_27","ja":"タグ_2|タグ_8|タグ_22|タグ_27"}}]},{"company_name":{"ko":"데이터얼라이언스(DataAlliance)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_27|태그_6|태그_11","en":"tag_27|tag_6|tag_11","ja":"タグ_27|タグ_6|タグ_11"}}]},{"company_name":{"ko":"쿼드자산운용","en":"쿼드자산운용","ja":""},"tags":[{"tag_name":{"ko":"태그_24|태그_23|태그_26|태그_29","en":"tag_24|tag_23|tag_26|tag_29","ja":"タグ_24|タグ_23|タグ_26|タグ_29"}}]},{"company_name":{"ko":"주식회사 링크드코리아","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_12|태그_6|태그_8","en":"tag_12|tag_6|tag_8","ja":"タグ_12|タグ_6|タグ_8"}}]},{"company_name":{"ko":"주렁주렁(zoolungzoolung)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_30|태그_17|태그_18","en":"tag_30|tag_17|tag_18","ja":"タグ_30|タグ_17|タグ_18"}}]},{"company_name":{"ko":"","en":"Amore Pacific_TEST","ja":""},"tags":[{"tag_name":{"ko":"태그_17|태그_27|태그_28|태그_6","en":"tag_17|tag_27|tag_28|tag_6","ja":"タグ_17|タグ_27|タグ_28|タグ_6"}}]},{"company_name":{"ko":"","en":"Luna Marketing Group","ja":""},"tags":[{"tag_name":{"ko":"태그_2|태그_18","en":"tag_2|tag_18","ja":"タグ_2|タグ_18"}}]},{"company_name":{"ko":"동신항운","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_26","en":"tag_26","ja":"タグ_26"}}]},{"company_name":{"ko":"히숲","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_11|태그_17|태그_7|태그_14","en":"tag_11|tag_17|tag_7|tag_14","ja":"タグ_11|タグ_17|タグ_7|タグ_14"}}]},{"company_name":{"ko":"COVENANT","en":"COVENANT","ja":""},"tags":[{"tag_name":{"ko":"태그_10|태그_3","en":"tag_10|tag_3","ja":"タグ_10|タグ_3"}}]},{"company_name":{"ko":"젠틀파이","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_18|태그_17|태그_4|태그_14","en":"tag_18|tag_17|tag_4|tag_14","ja":"タグ_18|タグ_17|タグ_4|タグ_14"}}]},{"company_name":{"ko":"아크로고스","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_15|태그_29|태그_27","en":"tag_15|tag_29|tag_27","ja":"タグ_15|タグ_29|タグ_27"}}]},{"company_name":{"ko":"페르소나미디어","en":"Persona Media","ja":""},"tags":[{"tag_name":{"ko":"태그_26|태그_13","en":"tag_26|tag_13","ja":"タグ_26|タグ_13"}}]},{"company_name":{"ko":"","en":"Rejoice Pregnancy","ja":""},"tags":[{"tag_name":{"ko":"태그_22|태그_30|태그_7|태그_4","en":"tag_22|tag_30|tag_7|tag_4","ja":"タグ_22|タグ_30|タグ_7|タグ_4"}}]},{"company_name":{"ko":"","en":"The Wave","ja":""},"tags":[{"tag_name":{"ko":"태그_3","en":"tag_3","ja":"タグ_3"}}]},{"company_name":{"ko":"","en":"CoCoon Foundation","ja":""},"tags":[{"tag_name":{"ko":"태그_26","en":"tag_26","ja":"タグ_26"}}]},{"company_name":{"ko":"스트라다월드와이드(Strada)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_9|태그_14|태그_11|태그_13","en":"tag_9|tag_14|tag_11|tag_13","ja":"タグ_9|タグ_14|タグ_11|タグ_13"}}]},{"company_name":{"ko":"도빗(Dobbit)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_29|태그_18|태그_21","en":"tag_29|tag_18|tag_21","ja":"タグ_29|タグ_18|タグ_21"}}]},{"company_name":{"ko":"지란지교시큐리티","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_26|태그_24|태그_10|태그_27","en":"tag_26|tag_24|tag_10|tag_27","ja":"タグ_26|タグ_24|タグ_10|タグ_27"}}]},{"company_name":{"ko":"캠퍼스멘토","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_29","en":"tag_29","ja":"タグ_29"}}]},{"company_name":{"ko":"삼일제약","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_2|태그_22","en":"tag_2|tag_22","ja":"タグ_2|タグ_22"}}]},{"company_name":{"ko":"제이에이치개발","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_27|태그_25|태그_6|태그_14","en":"tag_27|tag_25|tag_6|tag_14","ja":"タグ_27|タグ_25|タグ_6|タグ_14"}}]},{"company_name":{"ko":"오케이코인코리아","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_3|태그_25","en":"tag_3|tag_25","ja":"タグ_3|タグ_25"}}]},{"company_name":{"ko":"그릿연구소","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_25","en":"tag_25","ja":"タグ_25"}}]},{"company_name":{"ko":"세계정부 世界政府","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_15|태그_19|태그_11","en":"tag_15|tag_19|tag_11","ja":"タグ_15|タグ_19|タグ_11"}}]},{"company_name":{"ko":"투게더앱스","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_22|태그_10|태그_4|태그_28","en":"tag_22|tag_10|tag_4|tag_28","ja":"タグ_22|タグ_10|タグ_4|タグ_28"}}]},{"company_name":{"ko":"Dream Agility","en":"Dream Agility","ja":""},"tags":[{"tag_name":{"ko":"태그_19","en":"tag_19","ja":"タグ_19"}}]},{"company_name":{"ko":"대성시스템","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_2|태그_19","en":"tag_2|tag_19","ja":"タグ_2|タグ_19"}}]},{"company_name":{"ko":"바이럴네이션","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_8|태그_6|태그_20|태그_26","en":"tag_8|tag_6|tag_20|tag_26","ja":"タグ_8|タグ_6|タグ_20|タグ_26"}}]},{"company_name":{"ko":"오가나셀","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_11|태그_1","en":"tag_11|tag_1","ja":"タグ_11|タグ_1"}}]},{"company_name":{"ko":"디토나인","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_25|태그_29|태그_14","en":"tag_25|tag_29|tag_14","ja":"タグ_25|タグ_29|タグ_14"}}]},{"company_name":{"ko":"","en":"Haulio","ja":""},"tags":[{"tag_name":{"ko":"태그_3","en":"tag_3","ja":"タグ_3"}}]},{"company_name":{"ko":"대상홀딩스(주) - existing","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_23","en":"tag_23","ja":"タグ_23"}}]},{"company_name":{"ko":"만나씨이에이","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_15","en":"tag_15","ja":"タグ_15"}}]},{"company_name":{"ko":"지오코리아(페루관광청)","en":"GEOCM Co.","ja":"GEOCM"},"tags":[{"tag_name":{"ko":"태그_28|태그_17","en":"tag_28|tag_17","ja":"タグ_28|タグ_17"}}]},{"company_name":{"ko":"KFC Korea","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_17|태그_19","en":"tag_17|tag_19","ja":"タグ_17|タグ_19"}}]},{"company_name":{"ko":"까브드뱅(Cave de Vin)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_2|태그_10|태그_21","en":"tag_2|tag_10|tag_21","ja":"タグ_2|タグ_10|タグ_21"}}]},{"company_name":{"ko":"홈스토리생활","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_7|태그_20","en":"tag_7|tag_20","ja":"タグ_7|タグ_20"}}]},{"company_name":{"ko":"아이엠에이치씨(IMHC)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_4|태그_30|태그_19|태그_28","en":"tag_4|tag_30|tag_19|tag_28","ja":"タグ_4|タグ_30|タグ_19|タグ_28"}}]},{"company_name":{"ko":"플라이트그래프-탈퇴","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_30|태그_17|태그_9","en":"tag_30|tag_17|tag_9","ja":"タグ_30|タグ_17|タグ_9"}}]},{"company_name":{"ko":"YG PLUS","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_1|태그_16|태그_5","en":"tag_1|tag_16|tag_5","ja":"タグ_1|タグ_16|タグ_5"}}]},{"company_name":{"ko":"우리말소프트","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_13|태그_27|태그_24","en":"tag_13|tag_27|tag_24","ja":"タグ_13|タグ_27|タグ_24"}}]},{"company_name":{"ko":"아로마티카","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_29","en":"tag_29","ja":"タグ_29"}}]},{"company_name":{"ko":"","en":"Private Organization","ja":""},"tags":[{"tag_name":{"ko":"태그_24","en":"tag_24","ja":"タグ_24"}}]},{"company_name":{"ko":"스피링크","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_19|태그_9","en":"tag_19|tag_9","ja":"タグ_19|タグ_9"}}]},{"company_name":{"ko":"Onion Ground","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_6|태그_2","en":"tag_6|tag_2","ja":"タグ_6|タグ_2"}}]},{"company_name":{"ko":"브레이브팝스","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_28","en":"tag_28","ja":"タグ_28"}}]},{"company_name":{"ko":"Bidalgo","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_3|태그_13","en":"tag_3|tag_13","ja":"タグ_3|タグ_13"}}]},{"company_name":{"ko":"티엠씨케이","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_1|태그_26|태그_19|태그_17","en":"tag_1|tag_26|tag_19|tag_17","ja":"タグ_1|タグ_26|タグ_19|タグ_17"}}]},{"company_name":{"ko":"(주) 휴톰-중복","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_14|태그_15","en":"tag_14|tag_15","ja":"タグ_14|タグ_15"}}]},{"company_name":{"ko":"","en":"Chengbao","ja":""},"tags":[{"tag_name":{"ko":"태그_24|태그_16|태그_19|태그_29","en":"tag_24|tag_16|tag_19|tag_29","ja":"タグ_24|タグ_16|タグ_19|タグ_29"}}]},{"company_name":{"ko":"헬프미","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_26|태그_11|태그_16","en":"tag_26|tag_11|tag_16","ja":"タグ_26|タグ_11|タグ_16"}}]},{"company_name":{"ko":"(주) 새론다이내믹스","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_15|태그_14|태그_30|태그_29","en":"tag_15|tag_14|tag_30|tag_29","ja":"タグ_15|タグ_14|タグ_30|タグ_29"}}]},{"company_name":{"ko":"마상소프트","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_12","en":"tag_12","ja":"タグ_12"}}]},{"company_name":{"ko":"(주)아임블록","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_25","en":"tag_25","ja":"タグ_25"}}]},{"company_name":{"ko":"(주)이모션글로벌-중복","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_13|태그_21|태그_28","en":"tag_13|tag_21|tag_28","ja":"タグ_13|タグ_21|タグ_28"}}]},{"company_name":{"ko":"Altagram","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_25|태그_26","en":"tag_25|tag_26","ja":"タグ_25|タグ_26"}}]},{"company_name":{"ko":"이베스트투자증권","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_1|태그_20","en":"tag_1|tag_20","ja":"タグ_1|タグ_20"}}]},{"company_name":{"ko":"소굿마케팅","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_9|태그_10|태그_5","en":"tag_9|tag_10|tag_5","ja":"タグ_9|タグ_10|タグ_5"}}]},{"company_name":{"ko":"","en":"Grab","ja":""},"tags":[{"tag_name":{"ko":"태그_1","en":"tag_1","ja":"タグ_1"}}]},{"company_name":{"ko":"","en":"HK Yau","ja":""},"tags":[{"tag_name":{"ko":"태그_30","en":"tag_30","ja":"タグ_30"}}]},{"company_name":{"ko":"더락포트컴퍼니코리아-중복","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_7","en":"tag_7","ja":"タグ_7"}}]},{"company_name":{"ko":"휴마트컴퍼니","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_16|태그_29","en":"tag_16|tag_29","ja":"タグ_16|タグ_29"}}]},{"company_name":{"ko":"디센터","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_29|태그_7","en":"tag_29|tag_7","ja":"タグ_29|タグ_7"}}]},{"company_name":{"ko":"컬쳐히어로","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_11","en":"tag_11","ja":"タグ_11"}}]},{"company_name":{"ko":"보비어스코리아","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_11|태그_8|태그_3|태그_4","en":"tag_11|tag_8|tag_3|tag_4","ja":"タグ_11|タグ_8|タグ_3|タグ_4"}}]},{"company_name":{"ko":"베이글랩스","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_8|태그_18|태그_16","en":"tag_8|tag_18|tag_16","ja":"タグ_8|タグ_18|タグ_16"}}]},{"company_name":{"ko":"","en":"Katalis Digital","ja":""},"tags":[{"tag_name":{"ko":"태그_2|태그_16|태그_6|태그_18","en":"tag_2|tag_16|tag_6|tag_18","ja":"タグ_2|タグ_16|タグ_6|タグ_18"}}]},{"company_name":{"ko":"애디터(Additor)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_11|태그_2","en":"tag_11|tag_2","ja":"タグ_11|タグ_2"}}]},{"company_name":{"ko":"","en":"Avanade Asia Pte Ltd","ja":""},"tags":[{"tag_name":{"ko":"태그_8|태그_29|태그_15|태그_11","en":"tag_8|tag_29|tag_15|tag_11","ja":"タグ_8|タグ_29|タグ_15|タグ_11"}}]},{"company_name":{"ko":"500V2","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_11|태그_27","en":"tag_11|tag_27","ja":"タグ_11|タグ_27"}}]},{"company_name":{"ko":"플라이앤컴퍼니(푸드플라이)","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_29","en":"tag_29","ja":"タグ_29"}}]},{"company_name":{"ko":"영우디지탈-중복","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_14|태그_15|태그_7|태그_11","en":"tag_14|tag_15|tag_7|tag_11","ja":"タグ_14|タグ_15|タグ_7|タグ_11"}}]},{"company_name":{"ko":"","en":"Machipopo Inc.","ja":""},"tags":[{"tag_name":{"ko":"태그_19|태그_10|태그_4|태그_20","en":"tag_19|tag_10|tag_4|tag_20","ja":"タグ_19|タグ_10|タグ_4|タグ_20"}}]},{"company_name":{"ko":"시니어벤처스","en":"","ja":""},"tags":[{"tag_name":{"ko":"태그_20|태그_21|태그_6","en":"tag_20|tag_21|tag_6","ja":"タグ_20|タグ_21|タグ_6"}}]}]


    for r in request:
        requestCompanies = r['company_name'];
        requestTags = r['tags'];
        company_service.createCompany(requestCompanies, requestTags)

    return "test데이터 잘들어갔습니다.";

