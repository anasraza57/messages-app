<template>
    <div class="usersList">
      <a
        v-for="user in users"
        data-activity="1"
        data-last="1"
        data-uid="1"
        data-username="username"
        @click="() => openChat(user.id)"
        :class="['profileContainer', activeUser.id == user.id && 'active']"
        :key="user.id"
      >
        <!-- <div class="profileAvatar">
          <img src="https://via.placeholder.com/80" alt="Username" />
        </div> -->
        <div class="profileHolder">
          <div class="profileName">
            {{ user.username }}
          </div>
        </div>
        <div class="profileOptions">
          <div class="lastDate">
            <div class="dropdown">
              <button
                class="btn btn-secondary dropdown-toggle"
                type="button"
                id="dropdownMenuButton"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                <img src="../assets/dots-menu.png" alt="" class="img-fluid" />
              </button>
              <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <a class="dropdown-item" href="#">Delete</a>
              </div>
            </div>
          </div>
        </div>
      </a>
    </div>
</template>

<script>
export default {
    name: 'Message',

}
</script>

<style>

</style>