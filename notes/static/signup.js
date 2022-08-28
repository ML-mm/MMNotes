console.log('hello world')

const addUser = document.getElementById('add-user');


addUser.addEventListener('submit', (e) => {

    let formError = document.getElementById("form-errors");
    formError.innerHTML = "";

    e.preventDefault();
    let $this = $(addUser);
    let method = $this.attr('method');
    let endpoint = $this.attr('action');
    let data = $this.serialize();

    console.log($this)
    console.log(data)
    //if(XMLHttpRequest === '200') {}
    $.ajax({
        method: method,
        url: endpoint,
        data: data,
        dataType: 'json',
        success: function (response) {
            if (response.success) {
                console.log(response)
                console.log(data)
                window.location.href = '/' + '#useradded';
            }
            else {
                console.log(response.errors)
            }
        },
        error: function (response) {
            console.log(response)
            ctx = ``;
            let errors =  response.responseJSON.error;

            for(let error in errors){
                console.log(error)
                for(let text of errors[error]) {
                    ctx += `<p>${text}</p>`
                }
            }




            console.log(ctx);
            formError.innerHTML = ctx;
            //window.location.href = '/signup';
        }
    })
});