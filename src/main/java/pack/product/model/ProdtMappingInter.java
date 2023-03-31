package pack.product.model;

import java.util.List;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import pack.product.controller.ProdtBean;


@Mapper
public interface ProdtMappingInter {
	 //금융상품 목록 호출
	@Select("select * from FINANTIAL_PRODUCT")
	List<ProdtDto> selectProdtAll();
	
	//최신 금융상품 호출
	@Select("select * from FINANTIAL_PRODUCT where created_dt=(select max(created_dt) from FINANTIAL_PRODUCT where fin_prdt_type in('10','20','30'))")
	ProdtDto selectProdtRec();
	
	//최신 대출상품 호출
	@Select("select * from FINANTIAL_PRODUCT where created_dt=(select max(created_dt) from FINANTIAL_PRODUCT where fin_prdt_type in('40'))")
	ProdtDto selectLoanRec();
	
	 //금융상품 중복 여부 확인용 or 상품 상세 정보
	@Select("select * from FINANTIAL_PRODUCT where fin_prdt_code=#{fin_prdt_code}")
	ProdtDto selectProdt(String fin_prdt_code);
	
	 //금융 상품 생성
	@Insert("insert into FINANTIAL_PRODUCT(fin_prdt_code, kor_co_nm, fin_prdt_type, "
			+ "fin_prdt_nm, basic_rate, max_limit, created_user_id, "
			+ "created_dt, prodt_detail) values(#{fin_prdt_code}, #{kor_co_nm}, "
			+ "#{fin_prdt_type}, #{fin_prdt_nm}, #{basic_rate}, #{max_limit}, "
			+ "#{created_user_id}, now(), #{prodt_detail})")
	int insertProdt(ProdtBean bean);
	
	//////상품 메인페이지///////////////////
	//입출금 상품 호출
	@Select("select * from FINANTIAL_PRODUCT where created_dt=(select max(created_dt) from FINANTIAL_PRODUCT where fin_prdt_type in('10'))")
	ProdtDto selectAccountRec();
	//예금 상품 호출
	@Select("select * from FINANTIAL_PRODUCT where created_dt=(select max(created_dt) from FINANTIAL_PRODUCT where fin_prdt_type in('20'))")
	ProdtDto selectDepositRec();
	//적금 상품 호출
	@Select("select * from FINANTIAL_PRODUCT where created_dt=(select max(created_dt) from FINANTIAL_PRODUCT where fin_prdt_type in('30'))")
	ProdtDto selectSavingRec();
	//대출 전체상품 호출
	@Select("SELECT * "
			+ "FROM FINANTIAL_PRODUCT "
			+ "WHERE fin_prdt_type IN ('40') "
			+ "ORDER BY created_dt DESC "
			+ "LIMIT 3")
	List<ProdtDto> selectloanRecA();
	//상품 검색
	@Select("SELECT * FROM FINANTIAL_PRODUCT WHERE fin_prdt_nm LIKE '%${search}%' OR prodt_detail LIKE '%${search}%'")
	List<ProdtDto> getProdtSearch(ProdtBean search);
	////////////////////////////////////
}
