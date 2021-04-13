
# Parameters

    Name :                      CFv2TESTCAU2cf1-0
    Main :                      CFagentv2
    Level :                     Levels.Causal2
    Failed actions chance :     0.0
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        500000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      5
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      43206242155 function calls (43008730941 primitive calls) in 57309.98 seconds

##    Ordered by: cumulative time
   List reduced from 516 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57309.981 57309.981 {built-in method builtins.exec}
                      1    5.633    5.633 57309.981 57309.981 <string>:1(<module>)
                      1  190.618  190.618 57304.348 57304.348 main.py:103(CFagentv2)
                6854466   26.876    0.000 16004.539    0.002 agent.py:29(learn)
                6851477  412.250    0.000 12955.853    0.002 learner.py:42(Qlearn)
                2284822   12.512    0.000 10767.628    0.005 game.py:41(step)
                2284822   13.861    0.000 10304.858    0.005 layers.py:719(step)
        225031722/27522220  909.304    0.000 7316.021    0.000 module.py:866(_call_impl)
               18385921  215.224    0.000 6565.135    0.000 container.py:117(forward)
                2284822  239.015    0.000 6213.920    0.003 agent.py:54(_learn)
                9136299   73.848    0.000 6207.566    0.001 optimizer.py:84(wrapper)
               16055544   42.485    0.000 6092.182    0.000 network.py:24(forward)
                9136299   38.963    0.000 5885.263    0.001 grad_mode.py:24(decorate_context)
                9136299  257.877    0.000 5764.724    0.001 adam.py:55(step)
                2284822  236.275    0.000 5729.524    0.003 agent.py:202(_learn)
                2284822  205.968    0.000 5487.656    0.002 layers.py:17(step)
              226700454  361.199    0.000 5263.162    0.000 layer.py:98(move)
                9136299 1203.119    0.000 5238.955    0.001 _functional.py:53(adam)
                2284823  339.479    0.000 4780.388    0.002 layers.py:685(update)
                2284822 4236.441    0.002 4760.060    0.002 replaybuffer.py:85(sample_data)
                2284822  897.410    0.000 4441.830    0.002 agent.py:236(counterfact2)
                9136299   35.778    0.000 4202.768    0.000 tensor.py:195(backward)
                9136299   33.828    0.000 4165.731    0.000 __init__.py:68(backward)
                2284822   68.539    0.000 4020.560    0.002 agent.py:117(_learn)
                9136299 3960.198    0.000 3960.198    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2284822 3213.682    0.001 3898.133    0.002 replaybuffer.py:22(sample_data)
                2284822   39.520    0.000 3656.408    0.002 simulator.py:50(learn)
                2284822  239.532    0.000 3616.888    0.002 simulator.py:23(learn)
                2284822 2900.972    0.001 3556.376    0.002 replaybuffer.py:52(sample_data)
              226700454  663.813    0.000 3207.359    0.000 layers.py:736(check)
                4591857  121.068    0.000 2881.350    0.001 agent.py:49(__call__)
               39102219   86.717    0.000 2634.062    0.000 conv.py:398(forward)
               39102219   58.250    0.000 2503.675    0.000 conv.py:390(_conv_forward)
               39102219 2445.425    0.000 2445.425    0.000 {built-in method conv2d}
               30234653 2374.375    0.000 2374.375    0.000 {built-in method tensor}
                2284822  952.676    0.000 2363.668    0.001 agent.py:88(interveen)
               25164453   17.558    0.000 2258.021    0.000 game.py:37(board)
               31987515 1221.951    0.000 2122.914    0.000 layer.py:167(NoRock_update)
                2284822 1040.361    0.000 1851.253    0.001 replaybuffer.py:28(teleporter_save_data)
                4588207   43.357    0.000 1719.023    0.000 layers.py:741(restart)
               43596988   90.281    0.000 1681.265    0.000 linear.py:93(forward)
                2284822 1118.022    0.000 1664.788    0.001 agent.py:67(modify)
               43596988   36.152    0.000 1545.068    0.000 functional.py:1737(linear)
               43596988 1500.347    0.000 1500.347    0.000 {built-in method torch._C._nn.linear}
               38894797 1445.160    0.000 1445.160    0.000 {built-in method cat}
              226700454  256.909    0.000 1381.717    0.000 layers.py:730(isFree)
                4588207   21.775    0.000 1364.398    0.000 level.py:8(__init__)
                2284822 1053.855    0.000 1307.465    0.001 replaybuffer.py:91(simulator_save_data)
                4588207   52.158    0.000 1167.323    0.000 levels.py:151(generate)
             1198914684  980.771    0.000 1124.809    0.000 layer.py:95(isFree)
                2284822  853.913    0.000 1123.360    0.000 replaybuffer.py:58(CF_save_data)
              114349457 1102.700    0.000 1102.700    0.000 {built-in method clone}
               22026023  195.267    0.000 1062.290    0.000 level.py:41(notUsed)
              155308116 1029.456    0.000 1029.456    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2281833   43.289    0.000 1007.489    0.000 agent.py:171(__call__)
               64313286   56.508    0.000  957.952    0.000 activation.py:713(forward)
                2284822   41.720    0.000  933.860    0.000 agent.py:112(__call__)
                9136299  164.066    0.000  911.826    0.000 optimizer.py:189(zero_grad)
              155308116  901.808    0.000  901.808    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               64313286   54.014    0.000  901.444    0.000 functional.py:1364(leaky_relu)
             3836762582  625.945    0.000  899.873    0.000 enum.py:646(__hash__)
                6876679   44.290    0.000  856.117    0.000 agent.py:59(modify_board)
               64313286  837.413    0.000  837.413    0.000 {built-in method torch._C._nn.leaky_relu}
              228482300   99.884    0.000  822.243    0.000 {built-in method builtins.all}
                9207056  777.653    0.000  777.653    0.000 {built-in method torch._C._nn.one_hot}
             1152262427  290.966    0.000  749.952    0.000 layers.py:691(<genexpr>)
              226178916  175.791    0.000  734.720    0.000 {built-in method builtins.any}
                2330377    9.766    0.000  655.836    0.000 simulator.py:20(boardforward)
              226700454  425.859    0.000  653.396    0.000 layers.py:220(check)
              226700454  395.276    0.000  616.036    0.000 layers.py:208(check)
              226700454  394.899    0.000  610.286    0.000 layers.py:232(check)
               77654058  603.540    0.000  603.540    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1791152744  462.498    0.000  558.929    0.000 layers.py:701(<genexpr>)
              728242402  532.852    0.000  532.852    0.000 layer.py:146(elements)
               77654058  527.368    0.000  527.368    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                2284822   37.550    0.000  519.957    0.000 replaybuffer.py:18(stacker)
                2281833   39.192    0.000  500.148    0.000 replaybuffer.py:48(stacker)
               22026023   16.775    0.000  495.135    0.000 level.py:38(elementsIn)
               77654058  478.636    0.000  478.636    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               77654058  476.162    0.000  476.162    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                6854466  182.462    0.000  465.618    0.000 random.py:315(sample)
              543578496  334.568    0.000  416.337    0.000 tensor.py:906(grad)
              228482300  282.531    0.000  413.289    0.000 layers.py:114(isDone)
             4254763691  378.545    0.000  378.545    0.000 layer.py:91(positions)
                9136299   11.956    0.000  378.443    0.000 loss.py:527(forward)
                9136299   34.686    0.000  366.487    0.000 functional.py:2898(mse_loss)
                2284822   31.159    0.000  365.017    0.000 replaybuffer.py:81(stacker)
               33019475  360.622    0.000  360.622    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               77654058  357.683    0.000  357.683    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        4717457814/4717457810  310.524    0.000  351.949    0.000 {built-in method builtins.len}
                2284822  199.844    0.000  326.329    0.000 collector.py:46(collect)
               22026023  158.872    0.000  317.102    0.000 level.py:39(<listcomp>)
                4591857  109.280    0.000  302.068    0.000 exploration.py:53(softmaxer)
               32117449   26.785    0.000  300.274    0.000 layer.py:69(restart)
                9125146  296.376    0.000  296.376    0.000 {built-in method nonzero}
              226700454  181.697    0.000  274.817    0.000 layers.py:197(check)
             3836788821  273.933    0.000  273.933    0.000 {built-in method builtins.hash}
                2284822   46.125    0.000  256.794    0.000 agent.py:277(counterfact_check)
              125838346  248.945    0.000  248.945    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              333300447  181.122    0.000  235.042    0.000 layer.py:130(add)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9511601: <CFv2TESTCAU2cf1_0> in cluster <dcc> Done

Job <CFv2TESTCAU2cf1_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 12 20:13:40 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 12 20:22:23 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 20:22:23 2021
Terminated at Tue Apr 13 12:17:38 2021
Results reported at Tue Apr 13 12:17:38 2021

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

    CPU time :                                   57169.98 sec.
    Max Memory :                                 9281 MB
    Average Memory :                             6445.24 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7103.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57315 sec.
    Turnaround time :                            57838 sec.

The output (if any) is above this job summary.

