package pack.account.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

import pack.account.model.TransferDao;


@Controller
public class TransferController {
	
	@Autowired
	private TransferDao dao;
	
	
}
