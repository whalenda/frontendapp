package com.gulogulo.starterapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class NoMatch extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_no_match);
    }

    public void toMain(View view){
        Intent intent = new Intent(NoMatch.this, MainActivity.class);
        startActivity(intent);
    }
}
