
# Parameters

    Name :                      SuperLevel2_teleport-0
    Main :                      teleport
    Level :                     Levels.SuperLevel2
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      95408243650 function calls (95172115651 primitive calls) in 86104.89 seconds

##    Ordered by: cumulative time
   List reduced from 484 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86104.890 86104.890 {built-in method builtins.exec}
                      1    1.440    1.440 86104.890 86104.890 <string>:1(<module>)
                      1  182.897  182.897 86103.450 86103.450 main.py:45(teleport)
                4239966   18.658    0.000 31130.604    0.007 game.py:41(step)
                8479932   31.797    0.000 30513.768    0.004 agent.py:29(learn)
                4239966   21.345    0.000 29976.894    0.007 layers.py:718(step)
                8479932  710.655    0.000 26226.105    0.003 learner.py:42(Qlearn)
                4239966  398.122    0.000 21855.538    0.005 layers.py:17(step)
              423996600 1405.636    0.000 21418.805    0.000 layer.py:98(move)
                4239966  141.797    0.000 18289.318    0.004 agent.py:54(_learn)
              423996600 2458.437    0.000 15339.595    0.000 layers.py:735(check)
                4239966  118.262    0.000 12176.512    0.003 agent.py:117(_learn)
        265697491/29570503 1052.190    0.000 11688.494    0.000 module.py:715(_call_impl)
                8479932   54.895    0.000 11277.556    0.001 grad_mode.py:23(decorate_context)
                8479932  287.032    0.000 11123.425    0.001 adam.py:55(step)
               21090571   57.637    0.000 10946.687    0.001 network.py:27(forward)
               21090571  272.419    0.000 10766.179    0.001 container.py:115(forward)
                8479932 2046.986    0.000 9618.213    0.001 functional.py:53(adam)
                4239967  613.205    0.000 8072.887    0.002 layers.py:684(update)
                8370673  185.349    0.000 7104.022    0.001 agent.py:49(__call__)
                8479932   59.477    0.000 6039.683    0.001 tensor.py:181(backward)
                8479932   32.852    0.000 5980.206    0.001 __init__.py:68(backward)
                4239966 2460.907    0.001 5959.569    0.001 agent.py:88(interveen)
                8479932 5718.971    0.001 5718.971    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4239966 3010.574    0.001 4976.877    0.001 replaybuffer.py:22(sample_data)
                4239966 2497.046    0.001 4763.201    0.001 agent.py:67(modify)
                4239966 2355.743    0.001 4645.333    0.001 replaybuffer.py:28(teleporter_save_data)
               42181142   73.911    0.000 3906.196    0.000 conv.py:422(forward)
               42181142   81.900    0.000 3804.810    0.000 conv.py:414(_conv_forward)
              423996600  862.366    0.000 3797.324    0.000 layers.py:729(isFree)
               42181142 3708.749    0.000 3708.749    0.000 {built-in method conv2d}
               54791781  123.764    0.000 3501.968    0.000 linear.py:92(forward)
              423996600 2477.290    0.000 3422.449    0.000 layers.py:471(check)
               54791781  217.533    0.000 3323.748    0.000 functional.py:1669(linear)
               46639637 1798.030    0.000 3024.715    0.000 layer.py:151(update)
            11890078171 2097.180    0.000 3017.348    0.000 enum.py:646(__hash__)
             3829227706 2295.977    0.000 2934.958    0.000 layer.py:95(isFree)
             1185255217  755.432    0.000 2819.657    0.000 {built-in method builtins.any}
               54791781 2387.661    0.000 2387.661    0.000 {built-in method addmm}
              534235770 1458.042    0.000 2283.694    0.000 tensor.py:933(grad)
                4239966   57.310    0.000 2253.737    0.001 agent.py:112(__call__)
                8479932  221.354    0.000 2252.549    0.000 optimizer.py:167(zero_grad)
              423996600 1539.635    0.000 2174.089    0.000 layers.py:77(check)
               12610639   97.894    0.000 2131.413    0.000 agent.py:59(modify_board)
               33810469 2064.369    0.000 2064.369    0.000 {built-in method cat}
              152638776 1990.169    0.000 1990.169    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              423996600 1130.531    0.000 1909.866    0.000 layers.py:246(check)
              122542257 1866.786    0.000 1866.786    0.000 {built-in method clone}
              423996600 1048.785    0.000 1824.713    0.000 layers.py:286(check)
              152638776 1687.361    0.000 1687.361    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4239966   73.518    0.000 1662.836    0.000 replaybuffer.py:18(stacker)
             5021693796 1343.251    0.000 1654.504    0.000 layers.py:700(<genexpr>)
               18143567 1651.726    0.000 1651.726    0.000 {built-in method tensor}
               75882352   66.372    0.000 1622.894    0.000 activation.py:713(forward)
               75882352   98.829    0.000 1556.522    0.000 functional.py:1292(leaky_relu)
               75882352 1448.199    0.000 1448.199    0.000 {built-in method torch._C._nn.leaky_relu}
            13678477481 1333.588    0.000 1333.588    0.000 layer.py:91(positions)
               12610639 1325.345    0.000 1325.345    0.000 {built-in method torch._C._nn.one_hot}
                8479932   10.614    0.000 1300.987    0.000 game.py:37(board)
               29682896  162.712    0.000 1151.702    0.000 tensor.py:21(wrapped)
               76319388 1144.579    0.000 1144.579    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5522217   59.791    0.000 1127.641    0.000 layers.py:740(restart)
              695029088  389.093    0.000 1121.551    0.000 overrides.py:1070(has_torch_function)
                4239966  628.645    0.000 1055.116    0.000 collector.py:46(collect)
              453679596  121.742    0.000 1050.640    0.000 {built-in method builtins.all}
               76319388  999.533    0.000  999.533    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              903408908  215.701    0.000  962.938    0.000 layers.py:690(<genexpr>)
            11890109026  920.173    0.000  920.173    0.000 {built-in method builtins.hash}
               76319388  911.673    0.000  911.673    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               76319388  813.050    0.000  813.050    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8370673  269.652    0.000  757.571    0.000 exploration.py:53(softmaxer)
              423996600  483.683    0.000  752.065    0.000 layers.py:313(check)
              423996700  480.934    0.000  733.406    0.000 layers.py:113(isDone)
             1454209573  717.482    0.000  717.482    0.000 layer.py:146(elements)
              423996600  453.493    0.000  707.603    0.000 layers.py:273(check)
               76319388  647.084    0.000  647.084    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              423996600  427.352    0.000  626.093    0.000 layers.py:62(check)
              135152896  606.493    0.000  606.493    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
        6302246358/6302246356  435.802    0.000  568.599    0.000 {built-in method builtins.len}
                5522217   27.099    0.000  557.241    0.000 level.py:8(__init__)
              423996600  354.028    0.000  540.061    0.000 layers.py:48(check)
              388921396  196.511    0.000  505.787    0.000 random.py:285(choice)
                8479932   12.495    0.000  499.738    0.000 loss.py:445(forward)
               60744387   66.004    0.000  491.233    0.000 layer.py:69(restart)
               21199830  489.118    0.000  489.118    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                8479932   47.625    0.000  487.243    0.000 functional.py:2637(mse_loss)
              423996600  320.640    0.000  471.411    0.000 layers.py:23(check)
               54791781  469.110    0.000  469.110    0.000 {method 't' of 'torch._C._TensorBase' objects}
               25439796  421.251    0.000  421.251    0.000 {built-in method sum}
             5136376902  415.463    0.000  415.463    0.000 {method 'random' of '_random.Random' objects}
             1474532016  324.860    0.000  404.032    0.000 overrides.py:1083(<genexpr>)
              600972530  280.703    0.000  402.228    0.000 random.py:250(_randbelow_with_getrandbits)
              681199995  274.992    0.000  371.720    0.000 layer.py:130(add)
             3193168301  359.825    0.000  359.825    0.000 layer.py:203(isBlocking)
                8479932  308.152    0.000  308.152    0.000 {built-in method torch._C._nn.mse_loss}
               42181142   31.372    0.000  304.058    0.000 flatten.py:39(forward)
                5522217  180.129    0.000  298.152    0.000 levels.py:353(generate)
                5522317  138.275    0.000  295.677    0.000 layers.py:36(reset)
                4239966  109.963    0.000  295.671    0.000 random.py:315(sample)
              344341592  182.964    0.000  279.522    0.000 layer.py:126(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550911: <SuperLevel2_teleport_0> in cluster <dcc> Done

Job <SuperLevel2_teleport_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:50 2021
Job was executed on host(s) <n-62-11-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 24 07:24:14 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 07:24:14 2021
Terminated at Sun Apr 25 07:19:22 2021
Results reported at Sun Apr 25 07:19:22 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   86013.80 sec.
    Max Memory :                                 2682 MB
    Average Memory :                             2679.12 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13702.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86108 sec.
    Turnaround time :                            399452 sec.

The output (if any) is above this job summary.

