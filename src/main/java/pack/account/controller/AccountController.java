package pack.account.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import pack.account.model.AccountDao;
import pack.account.model.AccountDto;


@Controller
public class AccountController {
	
	@Autowired
	private AccountDao dao;
	
	@GetMapping("index")
	public String main() {
		return "index";
	}
	
	// 계좌 조회 하는 컨트롤러
	@GetMapping("view")
	public String viewAccount(HttpServletRequest request, Model model, HttpSession session) {
		if(session.getId().equals(null)) { 
			return "html.error/error";
		}else {
		String user_id = (String)session.getAttribute("user_id");
		AccountDto dto = dao.myAccount(user_id);
		model.addAttribute("info", dto);
		return "html.account/account";
		}
	}
	
	// 즉시 이체 첫 화면. session 없을 시 못들어온다.
	@GetMapping("directsend")
	public String send1(Model model, HttpSession session,@RequestParam("user_id")String user_id) {
		if (session.getAttribute("user_id") == user_id) {		
			AccountDto dto = dao.myAccount(user_id);
			model.addAttribute("info", dto);
			return "html.account/directsend1";	
		}else {
			return "error";
		}
	}
	
	// 사용자 요청값을 받아오고, 비밀번호 체크 과정 필요
	@PostMapping("directsend")
	public String send2(AccountBean bean, Model model,@RequestParam("user_id")String user_id,
			@RequestParam("account_passwd")String passwd, @RequestParam("account_number")String account_number,
			@RequestParam("user_name")String user_name) {
		
		AccountDto dto1 = dao.checkpass(user_id);
		if(dto1.getAccount_passwd().equals(passwd)) {		// 계좌비밀번호 일치 확인
			AccountDto dto2 = dao.checkaccount(user_name, account_number);		// 받는사람 이름과 계좌번호 일치하는 사람의 정보
			model.addAttribute("infosend",dto1);		// 사용자의 정보
			model.addAttribute("inforeceive",dto2);		// 이체 받는 사람의 정보
			return "html.account/directsend2";			
		}else {
			return "error";
		}
	}
	
	@GetMapping("directsend2")
	public String send3(AccountBean bean, Model model,@RequestParam("user_id")String user_id,
			@RequestParam("account_passwd")String passwd, @RequestParam("account_number")String account_number,
			@RequestParam("user_name")String user_name) {
		
		return "redirect:html.account/directsend3";
	}
	
	@GetMapping("autosend")
	public String auto1() {
		return "/html.account/autosend1";
	}
	
	@GetMapping("autosend2")
	public String auto2() {
		return "/html.account/autosend2";
	}
	
	@GetMapping("autosend3")
	public String auto3() {
		return "/html.account/autosend3";
	}
}
