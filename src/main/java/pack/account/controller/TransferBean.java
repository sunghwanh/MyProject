package pack.account.controller;

import lombok.Data;

@Data
public class TransferBean {
	private String transaction_no, account_no, transaction_type, transaction_result,amount, transaction_balance, take_account_number, take_fin_co_no,
	give_account_number, transacted_date;
	private String id, user_no,user_id, transaction_status, created_user_id, created_date;
}
