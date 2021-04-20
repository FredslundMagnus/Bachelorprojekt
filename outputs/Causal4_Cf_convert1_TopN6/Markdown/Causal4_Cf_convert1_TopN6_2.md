
# Parameters

    Name :                      Causal4_Cf_convert1_TopN6-2
    Main :                      CFagent
    Level :                     Levels.Causal4
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
    Cf convert :                1
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66930106452 function calls (66637018785 primitive calls) in 86117.81 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.809 86117.809 {built-in method builtins.exec}
                      1    4.874    4.874 86117.809 86117.809 <string>:1(<module>)
                      1  407.310  407.310 86112.935 86112.935 main.py:79(CFagent)
                9387087   50.031    0.000 24661.335    0.003 agent.py:29(learn)
                3129029   18.934    0.000 21704.556    0.007 game.py:41(step)
                3129029   22.410    0.000 20897.698    0.007 layers.py:718(step)
                9387086  649.477    0.000 19843.535    0.002 learner.py:42(Qlearn)
                3129029  326.387    0.000 13750.112    0.004 layers.py:17(step)
              312598481  968.220    0.000 13391.961    0.000 layer.py:98(move)
        327939903/34853927 1434.692    0.000 11439.602    0.000 module.py:866(_call_impl)
               25466841   78.196    0.000 10636.039    0.000 network.py:27(forward)
                3129029  969.034    0.000 10505.660    0.003 agent.py:210(counterfact)
               25466841  363.352    0.000 10371.614    0.000 container.py:117(forward)
                3129029  383.693    0.000 9628.535    0.003 agent.py:54(_learn)
                3129029  374.444    0.000 8717.411    0.003 agent.py:202(_learn)
              312598481 1514.424    0.000 8218.107    0.000 layers.py:735(check)
                3129029 6734.080    0.002 7809.662    0.002 replaybuffer.py:22(sample_data)
                9387086  103.437    0.000 7573.819    0.001 optimizer.py:84(wrapper)
                3129029 6182.774    0.002 7202.621    0.002 replaybuffer.py:67(sample_data)
                9387086   52.207    0.000 7159.064    0.001 grad_mode.py:24(decorate_context)
                3129030  491.806    0.000 7091.021    0.002 layers.py:684(update)
                9387086  334.876    0.000 6991.211    0.001 adam.py:55(step)
                9387086 1447.073    0.000 6310.240    0.001 _functional.py:53(adam)
                3129029  104.028    0.000 6241.620    0.002 agent.py:117(_learn)
                8036891  266.831    0.000 5702.118    0.001 agent.py:49(__call__)
               50063862 5440.714    0.000 5440.714    0.000 {built-in method tensor}
                9387086   44.052    0.000 5269.727    0.001 tensor.py:195(backward)
               42842024   29.300    0.000 5249.295    0.000 game.py:37(board)
                9387086   53.736    0.000 5224.308    0.001 __init__.py:68(backward)
                9387086 4955.468    0.001 4955.468    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               62580590 2895.396    0.000 4951.334    0.000 layer.py:151(update)
                3129029 1836.112    0.001 3992.750    0.001 agent.py:88(interveen)
               50933682  129.616    0.000 3848.574    0.000 conv.py:398(forward)
               50933682   81.631    0.000 3658.152    0.000 conv.py:390(_conv_forward)
               50933682 3576.521    0.000 3576.521    0.000 {built-in method conv2d}
                3129029 2059.818    0.001 3565.634    0.001 replaybuffer.py:28(teleporter_save_data)
              312598481  664.557    0.000 3539.599    0.000 layers.py:729(isFree)
               70142465  151.176    0.000 2916.536    0.000 linear.py:93(forward)
             2812889626 2410.812    0.000 2875.042    0.000 layer.py:95(isFree)
               70142465   57.817    0.000 2684.165    0.000 functional.py:1737(linear)
               70142465 2611.326    0.000 2611.326    0.000 {built-in method torch._C._nn.linear}
                3129029 1656.446    0.001 2535.068    0.001 agent.py:67(modify)
                1784807   42.572    0.000 2463.439    0.001 agent.py:175(choose_action)
               42456205 1697.496    0.000 1697.496    0.000 {built-in method cat}
             5963483286 1163.591    0.000 1684.840    0.000 enum.py:646(__hash__)
               11165920   87.149    0.000 1619.521    0.000 agent.py:59(modify_board)
                3129028   67.757    0.000 1537.998    0.000 agent.py:171(__call__)
               95609306   90.078    0.000 1525.068    0.000 activation.py:713(forward)
              142225313 1508.695    0.000 1508.695    0.000 {built-in method clone}
              312523160  341.081    0.000 1462.976    0.000 {built-in method builtins.any}
               95609306   84.195    0.000 1434.991    0.000 functional.py:1364(leaky_relu)
                3508870   48.700    0.000 1394.928    0.000 layers.py:740(restart)
                3129029   66.111    0.000 1392.402    0.000 agent.py:112(__call__)
               95609306 1334.529    0.000 1334.529    0.000 {built-in method torch._C._nn.leaky_relu}
              312598481 1018.271    0.000 1328.325    0.000 layers.py:77(check)
                3129029  997.040    0.000 1270.220    0.000 replaybuffer.py:73(CF_save_data)
             1105608198 1255.878    0.000 1255.878    0.000 layer.py:146(elements)
              175225604 1230.390    0.000 1230.390    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              312598481  782.862    0.000 1210.071    0.000 layers.py:286(check)
             3403335430  922.945    0.000 1121.894    0.000 layers.py:700(<genexpr>)
                9387086  203.401    0.000 1097.419    0.000 optimizer.py:189(zero_grad)
              175225604 1082.814    0.000 1082.814    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              312598481  653.214    0.000 1077.030    0.000 layers.py:246(check)
               11165920 1073.964    0.000 1073.964    0.000 {built-in method torch._C._nn.one_hot}
              312903000  172.827    0.000 1002.053    0.000 {built-in method builtins.all}
                3508870   23.767    0.000  980.436    0.000 level.py:8(__init__)
             1840793774  505.497    0.000  870.191    0.000 layers.py:690(<genexpr>)
                3129029   70.438    0.000  805.790    0.000 replaybuffer.py:18(stacker)
              312598481  621.152    0.000  791.698    0.000 layers.py:62(check)
                3508870  125.824    0.000  775.567    0.000 levels.py:199(generate)
                3129028   68.286    0.000  760.203    0.000 replaybuffer.py:63(stacker)
             7698773977  754.423    0.000  754.423    0.000 layer.py:91(positions)
               87612802  727.448    0.000  727.448    0.000 {method 'add' of 'torch._C._TensorBase' objects}
        8225270312/8225270309  575.594    0.000  639.211    0.000 {built-in method builtins.len}
               87612802  630.192    0.000  630.192    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                8036891  213.432    0.000  595.033    0.000 exploration.py:53(softmaxer)
              312598481  383.226    0.000  590.089    0.000 layers.py:313(check)
               87612802  584.601    0.000  584.601    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               87612802  582.308    0.000  582.308    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               13275798  223.164    0.000  579.335    0.000 random.py:315(sample)
              312598481  331.031    0.000  532.052    0.000 layers.py:273(check)
                7017740   63.254    0.000  524.705    0.000 level.py:41(notUsed)
              613289698  423.475    0.000  524.330    0.000 tensor.py:906(grad)
             5963518933  521.256    0.000  521.256    0.000 {built-in method builtins.hash}
                3129029  287.284    0.000  490.614    0.000 collector.py:46(collect)
              312598481  335.354    0.000  489.468    0.000 layers.py:48(check)
                9387086   21.696    0.000  480.994    0.000 loss.py:527(forward)
                9387086   52.360    0.000  459.299    0.000 functional.py:2898(mse_loss)
               87612802  424.178    0.000  424.178    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                1784807  372.215    0.000  372.215    0.000 agent.py:186(convert_values)
              312598481  240.123    0.000  358.447    0.000 layers.py:23(check)
               35088700   50.941    0.000  353.371    0.000 layer.py:69(restart)
              156520261  334.709    0.000  334.709    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              286340116  224.389    0.000  315.145    0.000 layer.py:126(remove)
              491270189  221.713    0.000  305.552    0.000 layer.py:130(add)
             3452543349  298.751    0.000  298.751    0.000 {method 'random' of '_random.Random' objects}
              385007713  188.765    0.000  280.155    0.000 random.py:250(_randbelow_with_getrandbits)
               62580590  274.967    0.000  274.967    0.000 layer.py:163(<listcomp>)
                9387086  273.991    0.000  273.991    0.000 {built-in method torch._C._nn.mse_loss}
                6258060  273.185    0.000  273.185    0.000 {built-in method nonzero}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533957: <Causal4_Cf_convert1_TopN6_2> in cluster <dcc> Done

Job <Causal4_Cf_convert1_TopN6_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:07 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 20:20:08 2021
Terminated at Mon Apr 19 20:15:41 2021
Results reported at Mon Apr 19 20:15:41 2021

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

    CPU time :                                   85904.71 sec.
    Max Memory :                                 9365 MB
    Average Memory :                             6414.63 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7019.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86238 sec.
    Turnaround time :                            86134 sec.

The output (if any) is above this job summary.

