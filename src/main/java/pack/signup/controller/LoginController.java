package pack.signup.controller;


import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

import pack.signup.model.LoginDao;
import pack.signup.model.LoginDto;



@Controller
public class LoginController {
	@Autowired
	private LoginDao loginDao;
	
	@GetMapping("login")
	public String login() {
		return "html.login/login";
	}
	
	@PostMapping("login")
	public String postLogin(HttpSession session,
			@RequestParam("id")String id,@RequestParam("passwd")String passwd) {
		LoginDto loginDto = loginDao.userLogin(id);
		
		if(loginDto != null) {
			String retName = loginDto.getUser_name();
			if(retName.equals(id)) {//사용자가 입력한 이름과 jikwon table의 이름이 같은 경우
				session.setAttribute("id", retName);
			}
		}
		return "redirect:/login";//로그인 성공하면 핵심로직 메소드 처리 결과 확인
	}
	
	@GetMapping("passwordfind")
	public String passwordfind(Model model) {
		return "html.login/passwordfind";
	}
	@GetMapping("signup")
	public String signup() {
		return "html.login/signup";
	}
	@GetMapping("userfind")
	public String userfind() {
		return "html.login/userfind";
	}
	@GetMapping("certificate")
	public String certificate() {
		return "html.login/certificate";
	}
	@GetMapping("certificate2")
	public String certificate2() {
		return "html.login/certificate2";
	}
	@PostMapping("logininsert")
	public String insetProcess(LoginBean bean) {
		boolean b = loginDao.insert(bean);
		
		if(b) {
			//return "list";  이러면안대 forward다 클라이언트주소가안바껴 pk error야 꼭 redirect해야되
			return "redirect:login";
			//return "redirect:list"; 둘다 사용해도 상관없음
		}else {
			return "redirect:http://localhost/err";
		}
	}
}
