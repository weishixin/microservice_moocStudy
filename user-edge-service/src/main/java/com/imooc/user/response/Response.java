package com.imooc.user.response;

import java.io.Serializable;

/**
 * @Author : weishixin
 * @Date : 2019/10/30
 */
public class Response implements Serializable {

    public static final Response USERNAME_PASSWORD_INVALID = new Response("1001", "username or password is error");

    public static final Response MOBILE_OR_EMAIL_REQUIRED = new Response("1002", "mobile or email is required");

    public static final Response SEND_VERIFY_CODE_FAILED = new Response("1003", "send verifyCode failed");

    public static final Response VERIFY_CODE_INVALID = new Response("1004", "verifyCode invalid");

    public static final Response CONNECT_SERVER_FAILED = new Response("9998", "connect server failed");

    public static final Response SUCCESS = new Response();

    private String code;
    private String message;

    public Response() {
        this.code = "0";
        this.message = "success";
    }

    public Response(String code, String message) {
        this.code = code;
        this.message = message;
    }

    public static Response exception(Exception e) {
        return new Response("9999", e.getMessage());
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
