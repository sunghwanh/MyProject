package pack.account.model;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class TransferDao {
	@Autowired
	private AccountInterface inter;
	
	
}
