let form = document.querySelector('.shade form')
let errorMessage = document.querySelector('.error')

handleSubmit(form)

function handleSubmit(form){
	form.addEventListener('submit', (e) => {
		e.preventDefault()
		var formData = new FormData(form)
		console.log(Array.from(formData))
		const url = "/bid/"
		fetch(url, {
			method: "post",
			body: formData
		})
		.then((res) => res.json())
		.then((data) => {
			console.log(data);
			if(data.message){
				form.reset()
				window.location.reload()
			}
		})
	})
}