import {polyfill} from 'es6-promise';
polyfill();

const BASE_URL = "http://doc.guojibu888.com/index.php?";
const STORE_URL = "http://192.168.199.121:5000";


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
        console.error(err);
        reject(false);
      }
    });
  });
};

export const postCliper = (data) => {
  return new Promise((resolve, reject) => {
    $.ajax({
      url: `${STORE_URL}/es`,
      method: 'post',
      beforeSend: function(request) {
        request.setRequestHeader("PW", "guojirenzheng123qwe");
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
