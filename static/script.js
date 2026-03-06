async function generateUseCase(){

const problem=document.getElementById("problem").value

document.getElementById("loading").style.display="block"
document.getElementById("result").value=""

const response=await fetch("/generate-usecase",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
problem
})

})

const data=await response.json()

document.getElementById("loading").style.display="none"

document.getElementById("result").value=data.result

}

function copyResult(){

const textarea=document.getElementById("result")

textarea.select()

document.execCommand("copy")

alert("Result copied!")

}