# NGINX Ansible Role

This role provides the NGINX web server with the opinionated H5BP server configuration.

Configuration overrides should be placed in `/etc/nginx/conf.d/`, and server definitions shoulf be placed in `/etc/nginx/server.d/`.

## Requirements

* Ansible 2.6+

## Role Variables

``` yaml
nginx_user: nginx
nginx_group: ~
nginx_worker_processes: auto
nginx_worker_rlimit_nofile: 8192
nginx_worker_connections: 8000
```

## Dependencies

None.

## Example Playbook

``` yaml
- hosts: localhost
  roles:
    - rchouinard.nginx
```

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
