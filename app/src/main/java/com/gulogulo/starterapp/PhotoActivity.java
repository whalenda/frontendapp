package com.gulogulo.starterapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class PhotoActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.found_photo);
    }

    public void gotodone(View view)
    {
        Intent intent = new Intent(PhotoActivity.this, info.class);
        startActivity(intent);
    }
}
