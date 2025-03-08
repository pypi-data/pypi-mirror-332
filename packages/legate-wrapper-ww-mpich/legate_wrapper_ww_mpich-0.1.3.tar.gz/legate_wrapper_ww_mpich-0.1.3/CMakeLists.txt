cmake_minimum_required(VERSION 3.22.1)

project(legate_wrapper)

# Check for environment variable if not set by -D option
if(NOT DEFINED LEGATE_WRAPPER_MPI_HOME AND DEFINED ENV{LEGATE_WRAPPER_MPI_HOME})
  set(LEGATE_WRAPPER_MPI_HOME $ENV{LEGATE_WRAPPER_MPI_HOME})
endif()

if(NOT DEFINED LEGATE_WRAPPER_MPI_NAME AND DEFINED ENV{LEGATE_WRAPPER_MPI_NAME})
  set(LEGATE_WRAPPER_MPI_NAME $ENV{LEGATE_WRAPPER_MPI_NAME})
endif()

option(LEGATE_WRAPPER_MPI_HOME "Path to MPI installation" "")
option(LEGATE_WRAPPER_MPI_NAME "Name of the MPI library" "")

if(LEGATE_WRAPPER_MPI_HOME)
  set(CMAKE_PREFIX_PATH ${LEGATE_WRAPPER_MPI_HOME} ${CMAKE_PREFIX_PATH})
endif()

set(MPI_NAME_SUFFIX "")
if(LEGATE_WRAPPER_MPI_NAME)
  set(MPI_NAME_SUFFIX "_${LEGATE_WRAPPER_MPI_NAME}")
endif()

set(LEGATE_MPI_WRAPPER_LIB_NAME "legate_mpi_wrapper${MPI_NAME_SUFFIX}")
add_subdirectory(legate_wrapper/legate_mpi_wrapper)

set(REALM_UCP_BOOTSTRAP_LIB_NAME "realm_ucp_bootstrap_mpi${MPI_NAME_SUFFIX}")
add_subdirectory(legate_wrapper/realm_ucp_bootstrap)
