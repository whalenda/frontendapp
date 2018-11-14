package com.gulogulo.starterapp;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import org.json.*;

import org.json.JSONObject;

public class PhotoActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.found_photo);
        if(getIntent().hasExtra("byteArray")) {
            ImageView previewThumbnail = (ImageView) findViewById(R.id.image);
            Bitmap b = BitmapFactory.decodeByteArray(
                    getIntent().getByteArrayExtra("byteArray"),0,getIntent().getByteArrayExtra("byteArray").length);
            previewThumbnail.setImageBitmap(b);
            try{
                JSONObject obj = new JSONObject(getIntent().getStringExtra("response"));
                String text = obj.getString("text");
                TextView t = (TextView) findViewById(R.id.description);
                t.setText(text);
                Log.d("yes", text);
            }
            catch (org.json.JSONException j){
                Log.d("jsonerror", j.toString());
            }
        }
    }

    public void gotodone(View view)
    {
        Intent intent = new Intent(PhotoActivity.this, info.class);
        intent.putExtra("response", getIntent().getStringExtra("response"));
        startActivity(intent);
    }
}
