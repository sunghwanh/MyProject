package pack.account.model;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.apache.ibatis.annotations.Update;

import pack.account.controller.AccountBean;


@Mapper
public interface AccountInterface {
	
	@Select("select * from account a join USER b on a.user_no=b.user_no join bank on fin_co_no=bank_code where user_id=#{param1}")
	AccountDto showmyAccount(String user_id);
	
	@Select("select * from account a join user b on a.user_no=b.user_no where user_id=#{param1}")
	AccountDto checkpassword(String user_id);
	
	@Select("select * from account a join user b on a.user_no=b.user_no where user_name=#{param1} and account_number=#{param2}")
	AccountDto checkaccount(String user_name, String account_number);
	
	@Update("update account set account_balance=account_balance-#{bean.account_balance} where user_id=#{bean.user_id}")
	int sendmoney(AccountBean bean);
	
	@Update("update account set account_balance=account_balance-#{bean.account_balance} where user_name=#{bean.user_name} and account_number=#{bean.account_number}")
	int receivemoney(AccountBean bean);
}
