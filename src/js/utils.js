import {polyfill} from 'es6-promise';
polyfill();

const BASE_URL = "http://doc.guojibu888.com/index.php?";

export const fetchCsrf = (getCsrfUrl) => {
  return new Promise((resolve, reject) => {
    $.ajax({
      url: `${BASE_URL}/csrf`,
      method: 'get',
      success: (data) => {
        resolve(data.data);
      },
      error: (err) => {
        console.log(err);
        reject(false);
      }
    });
  });
};

export const validateEmail = (email) => {
  return /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email);
};

export const getValidateEmail = (targetId) => {
  var email = document.getElementById(targetId).value;
    return email;
  if (email && validateEmail(email)) {
    return email;
  }
  return false;
};

export const getValidatePassword = (targetId) => {
  var password = document.getElementById(targetId).value;
    return password;
    if (password && password.length >= 8) {
    return password;
  }
  return false
};

export const signupOrLogin = (url, data) => {
    data = Object.assign(data, {
        isAjax: 1,
        checkCode: undefined,
        rememberPassword: 0
    })
  return new Promise((resolve, reject) => {
    $.ajax({
      url: `${BASE_URL}${url}`,
      data,
      method: 'get',
      success: (data) => {
        if (data.code) {
          resolve(data.data);
        } else {
          reject(false);
        }
      },
      error: (err) => {
        console.log(err);
        reject(false);
      }
    });
  });
};

export const fetchUserInfo = (userId) => {
  return new Promise((resolve, reject) => {
    $.ajax({
      url: `${BASE_URL}/user/${userId}/info`,
      method: 'get',
      success: (data) => {
        resolve(data.data);
      },
      error: (err) => {
        console.log(err);
        reject(false);
      }
    });
  });
};

export const postCliper = (data) => {
  return new Promise((resolve, reject) => {
    // var slogan = prompt("Input a slogan: ");
    // if ( slogan != nil ) {
    //   alert("Your slogan is "+ slogan );
    // }else {
    //   slogan = "null" ;
    // }
    $.ajax({
      url: `${BASE_URL}/es`,
      method: 'post',
      beforeSend: function(request) {
        request.setRequestHeader("PW", "guojirenzheng123qwe");
        //request.setRequestHeader("TAG", slogan);
      },
      data,
      success: (data) => {
        if (data.code) {
          resolve(true);
        } else {
          reject(false);
        }
      },
      error: (err) => {
        console.log(err);
        reject(false);
      }
    });
  });
};
