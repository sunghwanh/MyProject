package pack.mypage.controller;

import javax.servlet.http.HttpSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import pack.mypage.model.DataDao;
import pack.mypage.model.UserDto;

@Controller
public class MypageController {
	
	private Logger logger = LoggerFactory.getLogger(this.getClass());
	
	@Autowired
	private DataDao dao;
	
	// 마이페이지 메인 페이지로 이동
	@GetMapping("/mymain")
	public String mymain(HttpSession session, Model model) {
		UserDto dto = dao.getUserData((String)session.getAttribute("user_id"));
		model.addAttribute("userInfo",dto);
		return "html.mypage/mymain";
	}
	
	// 본인 정보 확인폼으로 이동
	@GetMapping("/myChkPwd")
	public String goChgPwd(HttpSession session) {
		// 임시 세션 생성
		//session.setAttribute("user_id", "aa");
		
		// model에 UserBean 타입의 빈 객체를 넘겨주기
		//model.addAttribute("bean",new UserBean());
		
		return "html.mypage/chkForm";
	}
	
	// 본인 인증 
	@PostMapping("/chkPwdInfo")
	public String chgPwdInfo(UserBean bean, HttpSession session,Model model) {
		String id=(String)session.getAttribute("user_id");
		bean.setUser_id(id);
		//logger.info(bean.getUser_id()+" "+bean.getUser_name()+" "+bean.getUser_jumin());
		boolean b=dao.chkPwdInfo(bean);
		
		if(b) {
			session.removeAttribute("executed");
			return "html.mypage/chgPwdForm";
		}else {
			model.addAttribute("result",b);
			return "html.mypage/chkForm";
		}
	}
	
	@PostMapping("chgpwd")
	public String chgpwd(UserBean bean ,HttpSession session,Model model) {
		bean.setUser_id((String) session.getAttribute("user_id"));
		
		boolean b = dao.updatePwd(bean);
		
		logger.info((String) session.getAttribute("user_id"));
		logger.info(bean.getUser_passwd());
		if(b) {
			// 비밀번호 변경시 세션 삭제
			//session.removeAttribute("user_id");
			UserDto dto = dao.getUserData((String)session.getAttribute("user_id"));
			model.addAttribute("userInfo",dto);
			return "html.mypage/mymain";
		}else {
			return "html.error/error";
		}
		
	}
}
