package pack.signup.model;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import pack.signup.controller.LoginBean;

@Mapper
public interface LoginMapperInterface {
	//@Insert("insert into USER values(#{bean.user_no},#{bean.user_id},#{bean.user_passwd},#{bean.user_name},#{bean.user_email},#{bean.user_jumin},#{bean.user_tel},#{bean.user_gen},#{bean.user_zipcode},#{bean.user_addr},#{bean.user_addr2}")
	//@Insert("insert into USER values(#{user_id},#{user_passwd},#{user_name},#{user_email},#{user_jumin},#{user_tel},#{user_gen},#{user_zipcode},#{user_addr},#{user_addr2},now(),now(),'logining',now(),'silver'")
	@Insert("insert into USER (user_id,user_passwd, user_name, user_email, user_jumin,user_tel, user_gen,user_zipcode,user_addr,user_addr2 ,user_regdate,user_status,last_login_dt,user_level) "
			+ "values (#{user_id},#{user_passwd},#{user_name},#{user_email},#{user_jumin},#{user_tel},#{user_gen},#{user_zipcode},#{user_addr},#{user_addr2},now(),'logining',now(),'silver')")
	int insertData(LoginBean bean);
	
	@Select("select * from USER where user_id=#{param1}")
	LoginDto userLogin(String user_id);
	
	@Select("select user_id,user_passwd,user_name from USER where user_id=#{param1} AND user_passwd=#{param2}")
	LoginDto userLoginCheck(String user_id, String user_passwd);
}
