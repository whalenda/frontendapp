package com.gulogulo.starterapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Home extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
    }
    public void gotologin(View view)
    {
        Intent intent = new Intent(Home.this, Login2.class);
        startActivity(intent);
    }
    public void gotoregister(View view){
        Intent intent = new Intent(Home.this, Register.class);
        startActivity(intent);
    }
}
