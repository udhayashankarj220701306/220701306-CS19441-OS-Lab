{
	name = $1;
	subjects_failed = 0;

	for(i = 2; i <= NF; i++){
		if($i < 45){
			subjects_failed++;
		}
	}

	if(subjects_failed > 0) {
		print name, "Fail";
	}else{
		print name, "Pass";
	}
}
