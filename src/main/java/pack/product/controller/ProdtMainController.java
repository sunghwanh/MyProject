package pack.product.controller;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import pack.product.model.ProdtDao;
import pack.product.model.ProdtDto;


@Controller
public class ProdtMainController {
	@Autowired
	private ProdtDao prodtDao;
	
	@GetMapping("prodtlist") //상품가입 메인상품 호출
	public String abc(Model model) {
		ProdtDto dto1 = prodtDao.selectProdtRec(); //대출 제외 최신상품
		ProdtDto dto2 = prodtDao.selectAccountRec(); //입출금 신상품
		ProdtDto dto3 = prodtDao.selectDepositRec(); //예금 신상품
		ProdtDto dto4 = prodtDao.selectSavingRec(); //적금 신상품
		model.addAttribute("data", dto1);
		model.addAttribute("data2", dto2);
		model.addAttribute("data3", dto3);
		model.addAttribute("data4", dto4);
		return "html.product/prodtlist";
	}
	
	@GetMapping("allprdtlist") //전체 상품 보기
	public String abcall(Model model) {
		ArrayList<ProdtDto> list = (ArrayList<ProdtDto>) prodtDao.selectProdtAll();
		model.addAttribute("datas", list);
		return "html.product/allprdtlist";
	}
	
	@GetMapping("testinsert_admin") //상품 추가 화면(관리자)
	public String abc2() {
		return "html.product/testinsert_admin";
	}
	
	@PostMapping("insert") //상품 추가 프로세스(관리자)
	public String abc3(ProdtBean bean) {
		boolean b = prodtDao.insertProdt(bean);
		if(b) {
			return "redirect:testlist1";
		}else {
			return "redirect:http://localhost/err" ;
		}
	}
	
	@GetMapping("prodtdetail") //상품 상세 정보(관리자), 금융 상품 코드 가져옴
	public String abc4(Model model, @RequestParam("fin_prdt_code") String fin_prdt_code) {
		ProdtDto dto = prodtDao.detailProdt(fin_prdt_code);
		model.addAttribute("datas", dto);
		return "html.product/prodtdetail";
	}
	
	@GetMapping("myprodtview") //가입한 상품 정보
	public String abc5() {
		return "html.product/myprodtview";
	}
	
	@GetMapping("loanprogress") //대출 진행 상황
	public String abc6() {
		return "html.product/loanprogress";
	}
	
	@GetMapping("myloan") //나의 대출 내역
	public String abc7() {
		return "html.product/myloan";
	}
	
	
	@GetMapping("search") //검색
	public String searchProcess(ProdtBean search, Model model) {
		ArrayList<ProdtDto> slist = (ArrayList<ProdtDto>) prodtDao.getProdtSearch(search);
		model.addAttribute("datas", slist);
		return "html.product/prodtsearchlist";
	}
	
	@GetMapping("loanlist") //대출 상품 신청
	public String abc8(Model model) {
		ProdtDto dto = prodtDao.selectLoanRec(); //메인 신상품 1개
		ArrayList<ProdtDto> list = (ArrayList<ProdtDto>) prodtDao.selectLoanRecA(); //신상품 3개
		model.addAttribute("rdata", dto);
		model.addAttribute("datas", list);
		return "html.product/loanlist";
	}
	
	@GetMapping("introprodt") //상품 안내
	public String abc9(String key) {
		return "html.product/introprodt";
	}
}
