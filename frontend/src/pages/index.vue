<template>
  <el-container class="fullscreen">
    <el-main>
      <el-row>
        <span class="grid-content">
           WASTE MANAGEMENT SYSTEM
          </span>
      </el-row>
      <el-row>
        <el-col :span="24">
          <span class="grid-content">
            Model
          </span>
          <span>
              <el-button type="text" @click="toTrain">
                <span class="grid-content"> Training</span>
              </el-button>
            </span>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24">
          <span class="grid-content bg-purple-dark">
            Model
          </span>
          <span>
            <el-button type="text" @click="getAccuracy()">
              <span class="grid-content">  accuracy</span>
            </el-button>
          </span>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="12">
          <span class="grid-content"> FCNN: </span>
          <span class="grid-content">{{ fcnn_accuracy }}</span>
        </el-col>
        <el-col :span="12">
          <span class="grid-content"> CNN: </span>
          <span class="grid-content">{{ cnn_accuracy }}</span>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24">
          <span class="grid-content bg-purple-dark">
            Model predictions
          </span>
        </el-col>
      </el-row>
      <el-row>
        <el-upload
            action="/upload"
            list-type="picture-card"
            :http-request="uploadSectionFile"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove">
          <i class="el-icon-plus"></i>
          <div slot="file" slot-scope="{file}">
            <img
                class="el-upload-list__item-thumbnail"
                :src="file.url" alt="">
            <span class="el-upload-list__item-actions">
                <span
                    class="el-upload-list__item-preview"
                    @click="handlePictureCardPreview(file)">
                    <i class="el-icon-zoom-in"></i>
                </span>
              </span>
          </div>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible">
          <span>cnn:{{ cnn_predicted }}</span>
          <span>fcnn:{{ fcnn_predicted }}</span>
          <img width="100%" :src="dialogImageUrl" alt="">
        </el-dialog>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import axios from "axios";

export default {
  name: 'admin',
  data() {
    return {
      disabled: false,
      dialogImageUrl: '',
      dialogVisible: false,
      fcnn_accuracy: '',
      cnn_accuracy: '',
      cnn_predicted: '',
      fcnn_predicted: ''
    }
  },
  mounted() {
  },
  methods: {
    uploadSectionFile(params) {
      const file = params.file;
      const form = new FormData();
      form.append('file', file);
      this.axios.post('/upload', form).then(res => {
        params.file.cnn = res.data.cnn_use
        params.file.fcnn = res.data.fcnn_use
        console.log(params.file)
      }).catch(() => {
      });
    },
    toTrain() {
      this.axios.get('/train').then(res => {
        if (res.status == 200) {
          this.$message("successs")
        }
      }).catch(res => {
        console.log(res.data)
      })
    },
    getAccuracy() {
      this.axios.get('/accuracy').then(res => {
        this.cnn_accuracy = res.data.cnn_accuracy
        this.fcnn_accuracy = res.data.fcnn_accuracy
      }).catch(res => {
        console.log(res.data)
      })
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePictureCardPreview(file) {
      console.log(file)
      this.dialogImageUrl = file.url;
      this.cnn_predicted = file.raw.cnn
      this.fcnn_predicted = file.raw.fcnn
      this.dialogVisible = true;
    },
  }
}
</script>

<style>
.fullscreen {
  height: 100vh;;
  background-image: url('https://stepbystepbusiness.com/wp-content/uploads/2022/06/How-to-Start-a-Waste-Management-Business_Thumbnail-1024x612.jpg');
  background-size: 100% 100%;
  background-position: center;
  background-repeat: no-repeat;
}

.el-menu {
  border: none;
}

.el-row {
  margin-bottom: 20px;
  border-radius: 2px;
  border: 1px red;

  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}


.bg-purple {
  background: #d3dce6;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  background: linear-gradient(to right, hsl(0, 100%, 50%), hsl(30, 100%, 50%), hsl(60, 100%, 50%), hsl(120, 100%, 50%), hsl(240, 100%, 50%), hsl(270, 100%, 50%), hsl(300, 100%, 50%));
  font-weight:bold;
  font-size: 40px;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  border-radius: 4px;
  min-height: 36px;
}

.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
</style>
