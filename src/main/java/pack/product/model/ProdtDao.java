package pack.product.model;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import pack.product.controller.ProdtBean;


@Repository
public class ProdtDao {
	private Logger logger = LoggerFactory.getLogger(this.getClass());

	@Autowired
	private ProdtMappingInter mappingInter;

	//전체 상품 목록 호출
	public List<ProdtDto> selectProdtAll() {
		List<ProdtDto> list = mappingInter.selectProdtAll();
		return list;
	}

	//대출 제외 최신상품 호출
	public ProdtDto selectProdtRec() {
		ProdtDto list = mappingInter.selectProdtRec();
		return list;
	}
	
	//대출 최신상품
	public ProdtDto selectLoanRec() {
		ProdtDto dto = mappingInter.selectLoanRec();
		return dto;
	}
	
	//입출금 신상품
	public ProdtDto selectAccountRec() {
		ProdtDto list = mappingInter.selectAccountRec();
		return list;
	}
	
	//예금 신상품
	public ProdtDto selectDepositRec() {
		ProdtDto list = mappingInter.selectDepositRec();
		return list;
	}
	
	//적금 신상품
	public ProdtDto selectSavingRec() {
		ProdtDto list = mappingInter.selectSavingRec();
		return list;
	}
	
	//대출 신상품(3개)
	public List<ProdtDto> selectLoanRecA(){
		List<ProdtDto> list = mappingInter.selectloanRecA();
		return list;
	}
	
	//상품 검색
	public List<ProdtDto> getProdtSearch(ProdtBean search){
		List<ProdtDto> slist = mappingInter.getProdtSearch(search);
		logger.info("datas : " + slist.size());
		return slist;
	}

	//상품 추가
	public boolean insertProdt(ProdtBean bean) {
		try {
			// 기존 데이터베이스에서 기본키 값이 있는지 검사
			/*
			 * ProdtDto existingDto = mappingInter.selectProdt(bean.getFin_prdt_code());
			 * if(existingDto!= null) { // 기존 데이터베이스에 기본키 값이 이미 존재하면 중복으로 처리 return false; }
			 */

			// 기존 데이터베이스에 기본키 값이 없으면 새로운 데이터를 추가
			int re = mappingInter.insertProdt(bean);
			if (re > 0) {
				return true;
			} else {
				return false;
			}
		} catch (Exception e) {
			logger.info("insertProdt 실패 : " + e.getMessage());
			return false;
		}
	}

	//상품 상세 정보
	public ProdtDto detailProdt(String code) {
		ProdtDto dto = mappingInter.selectProdt(code);
		return dto;
	}
}
