package pack.account.model;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import pack.account.controller.AccountBean;


@Repository
public class AccountDao {
	
	@Autowired
	private AccountInterface inter;
	
	// 조회창에서 보기 위해 정보 불러옴
	public AccountDto myAccount(String user_id) {
		AccountDto dto = inter.showmyAccount(user_id);
		return dto;
	}
	
	// 이체 전 사용자 비밀번호 확인
	public AccountDto checkpass(String user_id) {
		AccountDto dto = inter.checkpassword(user_id);
		return dto;
	}
	
	// 입금 받는 상대의 계좌 DB에 존재 여부 확인
	public AccountDto checkaccount(String user_name, String account_number) {
		AccountDto dto = inter.checkaccount(user_name, account_number);
		return dto;
	}
	
	
	// 즉시 이체 후 업데이트 하기 위한 메소드
	@Transactional
	public boolean directsend(AccountBean bean) {
		try {
			int re1 = inter.sendmoney(bean);
			int re2 = inter.receivemoney(bean);
			if(re1 > 0 && re2 > 0 ) {
				return true;
			}else {
				return false;
			}
		} catch (Exception e) {
			System.out.println("directsend error : " + e);
			return false;
		}
	}
	
}
