<template>
  <div>
    <b-button @click="sendEmail" variant="primary">
      <b-icon icon="envelope-fill"></b-icon> Send Email
    </b-button>
  </div>
</template>

<script>
export default {
  methods: {
    sendEmail() {
      const recipientEmail = 'recipient@example.com';
      const mailtoLink = `mailto:${recipientEmail}`;
      window.location.href = mailtoLink;
    },
  },
};
</script>
