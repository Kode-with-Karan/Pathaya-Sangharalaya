function submitFormLogin() {
    var form = document.getElementById('login-form');

    // Prevent the default form submission
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Your form handling logic here

        // For example, log the form data to the console

        var username = document.getElementById('your_name').value;
        var password = document.getElementById('your_pass').value;

        var formData = {
            username: username,
            password: password
        };

        fetch("../server/ip.json")
            .then(response => response.json())
            .then(data => {

                console.log(data)
                try {

                    fetch('http://' + data.IP[0].address + '/submit', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(formData)
                    })
                        .then(response => response.json())
                        .then(data => {
                            console.log(data.message);
                            if (data.message == '/') {
                                localStorage.setItem('userloginData', JSON.stringify(formData));
                                window.location.href = data.message;
                            }
                            else {
                                alert(data.message)
                            }
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });

                } catch (error) {

                    fetch('http://127.0.0.1:5000/submit', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(formData)
                    })
                        .then(response => response.json())
                        .then(data => {
                            console.log(data.message);
                            if (data.message == '/') {
                                localStorage.setItem('userloginData', JSON.stringify(formData));
                                window.location.href = data.message;
                            }
                            else {
                                alert(data.message)
                            }
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });

                }



            }
            )
    }
    )

}


function submitFormSignUp() {
    var form = document.getElementById('register-form');

    // Prevent the default form submission
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Your form handling logic here

        // For example, log the form data to the console

        var username = document.getElementById('name').value;
        var email = document.getElementById('email').value;
        var password = document.getElementById('pass').value;
        var repassword = document.getElementById('re_pass').value;

        var formData = {
            username: username,
            email: email,
            password: password,
            repassword: repassword
        };



        fetch("../server/ip.json")
            .then(response => response.json())
            .then(data => {

                console.log(data)
                try {

                    fetch('http://' + data.IP[0].address + '/signup', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(formData)
                    })
                        .then(response => response.json())
                        .then(data => {
                            console.log(data.message);
                            window.location.href = data.message;
                            // Handle the response as needed
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });


                } catch (error) {

                    fetch('http://127.0.0.1:5000/signup', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(formData)
                    })
                        .then(response => response.json())
                        .then(data => {
                            console.log(data.message);
                            window.location.href = data.message;
                            // Handle the response as needed
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });


                }

            })




    });

}