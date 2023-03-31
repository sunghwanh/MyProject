package pack.mypage.model;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import pack.mypage.controller.UserBean;

@Mapper
public interface DataMappingInterface {
	// 회원 정보 수정을 위해 화면에 기존 정보를 출력하기 위해 db에서 정보 읽어오기
	// session에 등록된 회원의 아이디를 이용
	@Select("select user_name, user_passwd, user_email, user_tel, user_zipcode, user_addr, user_addr2 from USER where user_id=#{user_id}")
	UserDto selectUser(String user_id);
	
	// 비밀번호 변경 전 아이디 & 이름 & 주민등록번호의 일치 여부 확인
	@Select("select * from USER where user_id=#{user_id} and user_name=#{user_name} and user_jumin=#{user_jumin}")
	UserDto chkPwdInfo(UserBean bean);
	
	// 비밀번호 변경
	@Update("update USER set user_passwd=#{user_passwd} where user_id=#{user_id}")
	int updatePwd(UserBean bean);
	
	// 수정한 회원 정보 db에 update
	//@Update("update USER set user_passwd=#{user_passwd}, user_email=#{user_email}, user_tel=#{user_tel}, user_zipcode=#{user_zipcode}, user_addr=#{user_addr}, user_addr2=#{user_addr2} where user_id=#{user_id}")
	//boolean updateUser(UserBean bean);
}
