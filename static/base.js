$(document).ready(function () {
    console.log("hello")
    $('#toggleForm').click(function () {
        console.log("clicked")
        $('#loginForm').slideToggle("slow");
    })
})

loginUser = document.getElementById('login-user')

loginUser.addEventListener('submit', (e) => {
    e.preventDefault()

    let $this = $(loginUser);
    let method = $this.attr('method');
    let endpoint = $this.attr('action')
    let data = $this.serialize()


    $.ajax({
        method: method,
        url: endpoint,
        data: data,
        dataType: 'json',
        success: function (response) {
            if (response.success) {
                console.log(response)
                window.location.href = '/' + '#signedin';
            }
            else {
                console.log(response.errors)
                window.location.href = '/' + '#notsignedin';
            }
        },
        error: function (response) {
            console.log(response)
            window.location.href = '/' + '#notsignedin';
        }
    })
})
