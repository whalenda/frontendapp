package com.gulogulo.starterapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import java.util.HashMap;
import java.util.Map;

public class Register extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
    }
    public void regin (View view) {
        EditText mEmailView = (EditText) findViewById(R.id.email);
        EditText mPasswordView = (EditText) findViewById(R.id.password);
        EditText confirmview = (EditText) findViewById(R.id.confirm);
        // Store values at the time of the login attempt.
        final String email = mEmailView.getText().toString();
        final String password = mPasswordView.getText().toString();
        final String confirm = confirmview.getText().toString();
        final String url = "http://35.237.212.25:8000/accounts/create";
        RequestQueue queue = Volley.newRequestQueue(this);
        // prepare the Request
        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>()
                {
                    @Override
                    public void onResponse(String response) {
                        Log.d("Response", response);
                        // TODO set session
                        // open main activity
                        Intent intent = new Intent(Register.this, MainActivity.class);
                        startActivity(intent);
                    }
                },
                new Response.ErrorListener()
                {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // set error
                        TextView errortext = (TextView) findViewById(R.id.errortext);
                        errortext.setText("invalid email or password");
                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams()
            {
                Map<String, String>  params = new HashMap<String, String>();
                params.put("email", email);
                params.put("password", password);
                params.put("confirm", confirm);

                return params;
            }
        };
        queue.add(postRequest);
    }
}
