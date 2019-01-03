function calc(){
		var x=document.getElementById("t").value;
		if(x=="")
			alert("Invalid Input");
		l=0;
		str="";
		arr=x.split(" ");
		for(i=0;i<arr.length;i++)
		{
			if(arr[i].length>l)
				l=arr[i].length;
			str=arr[i];
		}
		document.getElementById("word").innerHTML=str;
		document.getElementById("le").innerHTML=l;
	}