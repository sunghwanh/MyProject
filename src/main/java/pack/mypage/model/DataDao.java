package pack.mypage.model;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import pack.mypage.controller.UserBean;

@Repository
public class DataDao {
	private Logger logger = LoggerFactory.getLogger(this.getClass());
	
	@Autowired
	private DataMappingInterface mappingInterface;
	
	// 회원 수정 정보 읽어오기
	public UserDto getUserData(String user_id){
		UserDto uDto = mappingInterface.selectUser(user_id);
		
		logger.info("user Dto: "+uDto.getUser_name());
		
		return uDto;
	}
	
	// 비밀번호 변경 전 아이디 & 이름 & 주민등록번호의 일치 여부 확인
	public boolean chkPwdInfo(UserBean bean) {
		boolean b= false;
		UserDto userDto = mappingInterface.chkPwdInfo(bean);
		if(userDto!=null) {
			b=true;
		}
		return b;
	}
	
	// 비밀번호 변경
	public boolean updatePwd(UserBean bean) {
		int re=mappingInterface.updatePwd(bean);
		
		if(re>0) {	// 변경 성공
			return true;
		}else {
			return false;
		}
	}
}
