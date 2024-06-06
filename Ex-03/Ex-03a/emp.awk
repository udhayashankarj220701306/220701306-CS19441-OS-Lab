BEGIN {
	total_pay = 0;
	count = 0;
}

{
	name = $1;
	salary_per_day = $2;
	days_worked = $3;
	salary_earned = salary_per_day * days_worked;

	if(salary_earned > 6000 && days_worked > 4) {
		print name, salary_earned;
		total_pay += salary_earned;
		count++;
	}
}


END {
	if(count > 0){
		average_pay = total_pay / count;
		print "Total no of emp satisfying the criteria: ", count;
		print "Average pay of employees: ", average_pay;
	}else{
		print "No employees satisfy the criteria";
	}
}
