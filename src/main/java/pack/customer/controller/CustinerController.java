package pack.customer.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import pack.customer.business.CustomerBean;
import pack.customer.model.CustomerDao;
import pack.customer.model.CustomerDto;

@Controller
public class CustinerController {
	@Autowired
	private CustomerDao customerDao;
	
	
	@GetMapping("/mailconsult")
	public String mailconsult(Model model) {
		return "html.customer/mailconsult";
	}
	
	@GetMapping("/mailpassword")
	public String mailpassword(Model model, @RequestParam("customer_email_no")String customer_email_no) {
		model.addAttribute("data",customer_email_no);
		return "html.customer/mailpassword";
	}
	
	@GetMapping("/maildelete")
	public String mailDelete(Model model, @RequestParam("customer_email_no")String customer_email_no) {
	
		boolean b = customerDao.mailDelete(customer_email_no);
		if(b) {
			List<CustomerDto> slist= customerDao.customerMailSelect();
			model.addAttribute("datas",slist);
			return "html.customer/checkmail";
		}else {
			return "redirect:/error.html";
		}
	}
	
	@PostMapping("/mailupdate")
	public String mailUpdate(Model model, CustomerBean bean) {
		boolean b = customerDao.mailUpdate(bean);
		if(b) {
			List<CustomerDto> slist= customerDao.customerMailSelect();
			model.addAttribute("datas",slist);
			return "html.customer/checkmail";
		}else {
			return "redirect:/error.html";
		}
	}
	
	@PostMapping("/upDelpage")
	public String mailPasscheck(Model model,CustomerBean bean,
								@RequestParam("customer_email_name")String customer_email_name,
								@RequestParam("customer_email_password")String customer_email_password,
								@RequestParam("customer_email_no")String customer_email_no) {
		
		CustomerDto dto = (CustomerDto)customerDao.updateSelect(customer_email_no);
		
		if((dto.getCustomer_email_name().equals(bean.getCustomer_email_name()) ) &&
				dto.getCustomer_email_password().equals(bean.getCustomer_email_password())) {
			
			model.addAttribute("data",dto);
			return "html.customer/updatemail";
		}else {
			
			return "html.customer/error";
		}
	}
	
	
	@GetMapping("/chatconsult")
	public String productmain() {
		return "html.customer/chatconsult";
	}

	@GetMapping("/checkmail")
	public String checkmail(Model model) {
		List<CustomerDto> slist= customerDao.customerMailSelect();
	
		model.addAttribute("datas",slist);
		return "html.customer/checkmail";
	}	
	
	@GetMapping("/faq")
	public String Aspec_faq(Model model, String customer_faq_category,
			HttpServletRequest request, HttpServletResponse response) {
		
		if(customer_faq_category == null) {
			customer_faq_category = "조회/출금";
		}

		List<CustomerDto> slist= customerDao.CustomerFaqList(customer_faq_category);
		model.addAttribute("datas",slist);
		return "html.customer/faq";
	}
	
	@PostMapping("/mailconsult")
	public String loginpage(Model model,CustomerBean bean) {
		bean.setCustomer_email_date();
		boolean b = customerDao.customerInsert(bean);
		if(b) {
			List<CustomerDto> slist= customerDao.customerMailSelect();
			model.addAttribute("datas",slist);
			return "html.customer/checkmail";
		}else {
			return "redirect:/error.html";
		}
	}
	
	
	@PostMapping("/faqlist")
	@ResponseBody
	public Map<String, Object> customerProcess(@RequestParam("category")String customer_faq_category){
		List<Map<String, String>> list = new ArrayList<Map<String, String>>();
		Map<String, String> data = null;
		for(CustomerDto s:customerDao.CustomerFaqList(customer_faq_category)) {
			data = new HashMap<String, String>();
			data.put("customer_faq_question", s.getCustomer_faq_question());
			data.put("customer_faq_answer", s.getCustomer_faq_answer());
			list.add(data);
		}
		
		Map<String, Object> faqList = new HashMap<String, Object>();
		
		faqList.put("datas", list);
		
		return faqList;
	}
	
}
