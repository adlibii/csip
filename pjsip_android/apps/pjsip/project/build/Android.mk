LOCAL_PATH := $(call my-dir)
TOP_LOCAL_PATH := $(call my-dir)/../

#Add target arm version
ifeq ($(TARGET_ARCH_ABI),armeabi-v7a)
MY_PJSIP_FLAGS := $(BASE_PJSIP_FLAGS) -DPJ_HAS_FLOATING_POINT=1
else
MY_PJSIP_FLAGS := $(BASE_PJSIP_FLAGS) -DPJ_HAS_FLOATING_POINT=0
endif

# Pjsip
include $(TOP_LOCAL_PATH)/pjlib/build/Android.mk
include $(TOP_LOCAL_PATH)/pjlib-util/build/Android.mk
include $(TOP_LOCAL_PATH)/pjnath/build/Android.mk
include $(TOP_LOCAL_PATH)/pjmedia/build/Android.mk
include $(TOP_LOCAL_PATH)/pjsip/build/Android.mk

# Third parties
include $(TOP_LOCAL_PATH)/third_party/build/resample/Android.mk
##Secure third parties

HAS_OPENSSL := 0
#TLS
ifeq ($(MY_USE_TLS),1)
include $(TOP_LOCAL_PATH)/third_party/openssl/Android.mk
HAS_OPENSSL := 1
endif

#SRTP
include $(TOP_LOCAL_PATH)/third_party/build/srtp/Android.mk

#ZRTP
ifeq ($(MY_USE_ZRTP),1)
include $(TOP_LOCAL_PATH)/third_party/openssl/Android.mk
include $(TOP_LOCAL_PATH)/third_party/build/zrtp/Android.mk	
endif

##Media third parties
ifeq ($(MY_USE_ILBC),1)
	include $(TOP_LOCAL_PATH)/third_party/build/ilbc/Android.mk
endif
ifeq ($(MY_USE_GSM),1)
	include $(TOP_LOCAL_PATH)/third_party/build/gsm/Android.mk
endif
ifeq ($(MY_USE_SPEEX),1)
	include $(TOP_LOCAL_PATH)/third_party/build/speex/Android.mk
endif
ifeq ($(MY_USE_G729),1)
	include $(TOP_LOCAL_PATH)/third_party/build/g729/Android.mk
endif
ifeq ($(MY_USE_SILK),1)
	include $(TOP_LOCAL_PATH)/third_party/build/silk/Android.mk
endif


# pjsip JNI
include $(TOP_LOCAL_PATH)/jni/Android.mk

