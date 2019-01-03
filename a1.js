function calc(){
		var x=document.getElementById("num").value;
		if(x=="")
			alert("Enter a Value");
		else if(x<0)
			alert("Enter a positive Value");
		else{
		if(x%3==0 && x%7==0)
			document.getElementById("res").innerHTML="Divisible by 3 and 7";
		else if(x%3==0 && x%7!=0)
			document.getElementById("res").innerHTML="Divisible by 3";
		else if(x%3!=0 && x%7==0)
			document.getElementById("res").innerHTML="Divisible by7";
		else
			document.getElementById("res").innerHTML="Not Divisible";
		}
}