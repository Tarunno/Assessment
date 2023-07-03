let input = document.querySelectorAll('.deshboard input')
let label = document.querySelectorAll('.deshboard label')
let form = document.querySelector('.deshboard form')
let errorMessage = document.querySelector('.error')

let modal = document.querySelector('.modal')
let add_acution = document.querySelector('.add-auction')
let close = document.querySelector('.close')

add_acution.addEventListener('click', () => {
  modal.style.display = 'flex'
})
close.addEventListener('click', () => {
  modal.style.display = 'none'
})

handleInput(input, label)
handleSubmit(form, input, errorMessage)

function handleInput(input, label){
	input.forEach((el, index) => {
		const handleLabel = (e) => {
			label.forEach((lv, ix) => {
				lv.style.top = '28px'
				lv.style.fontSize = '15px'
				if(input[ix].value !== ''){
					lv.style.top = '10px'
					lv.style.fontSize = '10px'
				}
			})
			if(e.type == 'focusin'){
				label[index].style.top = '10px'
				label[index].style.fontSize = '10px'
			}
		}
		el.addEventListener('focusin', handleLabel)
		el.addEventListener('focusout', handleLabel)
	})
}

function handleSubmit(form, input, error){
	form.addEventListener('submit', (e) => {
		e.preventDefault()
		var formData = new FormData(form)
		console.log(Array.from(formData))
		const url = "/user/add/"
		fetch(url, {
			method: "post",
			body: formData
		})
		.then((res) => res.json())
		.then((data) => {
			console.log(data);
			if(data.message){
				errorMessage.innerHTML = ' ' + data.message
        errorMessage.style.borderLeft = '2px solid green'
				errorMessage.style.color = "green"
				form.reset()
				window.location.reload()
			}
		})
	})
}

function handleInputError(field, error ){
	if(error){
		field.style.background = 'rgba(255, 0, 0, .05)'
	}
	else{
		field.style.background = 'white'
	}
}