function calc(){
			var x=document.getElementById("num1").value;
			var y=document.getElementById("num2").value;

			if(x=="" || y=="")
				alert("Invalid input");
			else{
				if(document.getElementById("add").checked){
					a=parseInt(x);
					b=parseInt(y);
					document.getElementById("res").innerHTML=a+b;
				}
				else if(document.getElementById("sub").checked)
					document.getElementById("res").innerHTML=x-y;
				else if(document.getElementById("mul").checked)
					document.getElementById("res").innerHTML=x*y;
				else if(document.getElementById("div").checked){
					if(y!=0)
					document.getElementById("res").innerHTML=x/y;
					else
						alert("Divide By 0 Error");
			}
	}
}