package pack.signup.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import pack.signup.model.LoginDao;
import pack.signup.model.LoginDto;

@Controller
public class loginSuccessController {
	@Autowired
	private LoginDao loginDao; 
	
	@PostMapping("loginSuccess")
	public String loginSuccess(LoginBean bean,String user_id, String user_passwd,HttpServletResponse response,
			HttpServletRequest request, Model model) {
		LoginDto dto = loginDao.userLoginCheck(user_id, user_passwd);
		
		String user_name = dto.getUser_name();
		int user_no = dto.getUser_no();
		try {
			if (dto.getUser_id().equals(bean.getUser_id()) && dto.getUser_passwd().equals(bean.getUser_passwd())) {
				HttpSession session = request.getSession();
				 session.setMaxInactiveInterval(600);
				 session.setAttribute("user_id",user_id); 
				 session.setAttribute("user_name", user_name);
				 session.setAttribute("user_no", user_no);
				 
				return "index";
			}
			
		} catch (Exception e) {
		
		}
		return "html.error/error";
	}
	
	@GetMapping("logout")
	public String logout(HttpServletRequest request) {
		HttpSession session = request.getSession(true);
		session.removeAttribute("user_id");
		session.removeAttribute("user_name");
		session.removeAttribute("user_no");
		return "index";
	}
}
