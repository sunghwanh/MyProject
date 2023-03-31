package pack.signup.model;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import pack.signup.controller.LoginBean;

@Repository
public class LoginDao {
	private Logger logger = LoggerFactory.getLogger(this.getClass());

	@Autowired
	private LoginMapperInterface mapperInterface;

	// 회원가입
	public boolean insert(LoginBean bean) {

		try {
			int re = mapperInterface.insertData(bean);
			if (re > 0)
				return true;
			else
				return false;
		} catch (Exception e) {
			logger.info("insert fail :" + e.getMessage());
			return false;
		}
	}

	// 로그인
	public LoginDto userLogin(String user_id) {
		LoginDto dto = (LoginDto) mapperInterface.userLogin(user_id);
		return dto;
	}
	
	//로그인 체크
	public LoginDto userLoginCheck(String user_id, String user_passwd) {
		LoginDto dto = (LoginDto) mapperInterface.userLoginCheck(user_id,user_passwd);
		
		return dto;	
		
	}
}
