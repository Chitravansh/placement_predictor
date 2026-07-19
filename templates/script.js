
const API = " http://127.0.0.1:8000"

async function predict (){

    const cgpa = document.getElementById("cgpa").value;

    const iq = document.getElementById("iq").value;

    const response = await fetch(API + "/predict",{
        method : "POST",
        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            cgpa:Number(cgpa),
            iq:Number(iq)
        })
    });


    const data = await response.json();

    if(data.placement==1)
        document.getElementById("result").innerHTML="✔️ Placement will Take place";

    else 
        document.getElementById("result").innerHTML="😶 Placement Chances are low";

}