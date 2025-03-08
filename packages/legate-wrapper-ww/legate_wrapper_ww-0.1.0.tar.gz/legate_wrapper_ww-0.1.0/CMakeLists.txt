cmake_minimum_required(VERSION 3.22.1)

project(legate_wrapper)

option(MPI_HOME "Path to MPI installation" "")
option(MPI_NAME "Name of the MPI library" "")

if(MPI_HOME)
  set(CMAKE_PREFIX_PATH ${MPI_HOME} ${CMAKE_PREFIX_PATH})
endif()

set(MPI_NAME_SUFFIX "")
if(MPI_NAME)
  set(MPI_NAME_SUFFIX "_${MPI_NAME}")
endif()

set(LEGATE_MPI_WRAPPER_LIB_NAME "legate_mpi_wrapper${MPI_NAME_SUFFIX}")
add_subdirectory(legate_wrapper/legate_mpi_wrapper)

set(REALM_UCP_BOOTSTRAP_LIB_NAME "realm_ucp_bootstrap_mpi${MPI_NAME_SUFFIX}")
add_subdirectory(legate_wrapper/realm_ucp_bootstrap)
