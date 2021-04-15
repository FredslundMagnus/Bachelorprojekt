
# Parameters

    Name :                      ReTest15-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      59167723444 function calls (58908653965 primitive calls) in 86117.44 seconds

##    Ordered by: cumulative time
   List reduced from 511 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.443 86117.443 {built-in method builtins.exec}
                      1    4.246    4.246 86117.443 86117.443 <string>:1(<module>)
                      1  512.083  512.083 86113.197 86113.197 main.py:75(CFagent)
                9686976   60.826    0.000 28929.361    0.003 agent.py:29(learn)
                9684744  776.085    0.000 22965.199    0.002 learner.py:42(Qlearn)
                3228992   23.411    0.000 21007.469    0.007 game.py:41(step)
                3228992   25.687    0.000 20128.409    0.006 layers.py:718(step)
                3228992  353.258    0.000 13636.478    0.004 layers.py:17(step)
              322619262 1332.352    0.000 13253.190    0.000 layer.py:98(move)
        291417845/32350057 1419.367    0.000 11705.848    0.000 module.py:866(_call_impl)
                3228992  509.470    0.000 11225.117    0.003 agent.py:54(_learn)
               22665313   82.203    0.000 10748.138    0.000 network.py:24(forward)
               22665313  355.617    0.000 10474.427    0.000 container.py:117(forward)
                3228992  505.356    0.000 10127.338    0.003 agent.py:202(_learn)
                9684744  133.695    0.000 8514.598    0.001 optimizer.py:84(wrapper)
                9684744   68.878    0.000 7960.346    0.001 grad_mode.py:24(decorate_context)
              322619262 1239.721    0.000 7875.285    0.000 layers.py:735(check)
                3228992 6486.756    0.002 7805.428    0.002 replaybuffer.py:22(sample_data)
                9684744  390.308    0.000 7739.814    0.001 adam.py:55(step)
                3228992  142.195    0.000 7484.300    0.002 agent.py:117(_learn)
                9684744 1649.530    0.000 6964.971    0.001 _functional.py:53(adam)
                3228992 5701.590    0.002 6942.352    0.002 replaybuffer.py:52(sample_data)
                3228993  532.725    0.000 6422.533    0.002 layers.py:684(update)
                9684744   56.194    0.000 6308.917    0.001 tensor.py:195(backward)
                9684744   64.569    0.000 6251.160    0.001 __init__.py:68(backward)
                9684744 5908.219    0.001 5908.219    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3228992  738.129    0.000 5456.799    0.002 agent.py:210(counterfact)
                6485245  273.877    0.000 5453.828    0.001 agent.py:49(__call__)
                3228992 1920.733    0.001 4507.138    0.001 agent.py:88(interveen)
               45205895 2432.236    0.000 4105.998    0.000 layer.py:151(update)
               45330626  123.900    0.000 4064.072    0.000 conv.py:398(forward)
               45330626  103.558    0.000 3878.662    0.000 conv.py:390(_conv_forward)
               45330626 3775.105    0.000 3775.105    0.000 {built-in method conv2d}
                3228992 2112.926    0.001 3637.579    0.001 replaybuffer.py:28(teleporter_save_data)
               40499738 3536.375    0.000 3536.375    0.000 {built-in method tensor}
               33057700   24.743    0.000 3305.141    0.000 game.py:37(board)
              322619262  534.468    0.000 3131.264    0.000 layers.py:729(isFree)
                3228992 1848.013    0.001 2970.899    0.001 agent.py:67(modify)
               61537955  144.914    0.000 2944.464    0.000 linear.py:93(forward)
               61537955   62.722    0.000 2718.970    0.000 functional.py:1737(linear)
               61537955 2643.335    0.000 2643.335    0.000 {built-in method torch._C._nn.linear}
             2194820444 2249.760    0.000 2596.797    0.000 layer.py:95(isFree)
              322619262 1754.777    0.000 2439.236    0.000 layers.py:471(check)
              322619262 1608.165    0.000 2153.599    0.000 layers.py:77(check)
               41992997 2059.175    0.000 2059.175    0.000 {built-in method cat}
                3226760   86.756    0.000 1851.821    0.001 agent.py:171(__call__)
                9714237  104.195    0.000 1719.546    0.000 agent.py:59(modify_board)
                3228992   79.236    0.000 1599.584    0.000 agent.py:112(__call__)
              145161214 1530.105    0.000 1530.105    0.000 {built-in method clone}
               84203268   94.743    0.000 1476.226    0.000 activation.py:713(forward)
             5547765863 1033.437    0.000 1473.807    0.000 enum.py:646(__hash__)
               84203268   88.330    0.000 1381.482    0.000 functional.py:1364(leaky_relu)
                3228992 1092.983    0.000 1380.874    0.000 replaybuffer.py:58(CF_save_data)
              180778912 1321.453    0.000 1321.453    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               84203268 1278.527    0.000 1278.527    0.000 {built-in method torch._C._nn.leaky_relu}
                1320191   20.326    0.000 1237.708    0.001 layers.py:740(restart)
                9684744  223.337    0.000 1194.422    0.000 optimizer.py:189(zero_grad)
              180778912 1165.063    0.000 1165.063    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              324808102  281.247    0.000 1149.533    0.000 {built-in method builtins.any}
                9714237 1130.650    0.000 1130.650    0.000 {built-in method torch._C._nn.one_hot}
              322899300  122.430    0.000 1108.739    0.000 {built-in method builtins.all}
                1320191    9.721    0.000 1068.801    0.001 level.py:8(__init__)
              892779296 1064.864    0.000 1064.864    0.000 layer.py:146(elements)
             1203454450  344.986    0.000 1029.770    0.000 layers.py:690(<genexpr>)
                3228992   79.303    0.000 1007.309    0.000 replaybuffer.py:18(stacker)
                1320191   65.208    0.000  972.258    0.001 levels.py:262(generate)
                3226760   73.421    0.000  941.992    0.000 replaybuffer.py:48(stacker)
              322619262  737.518    0.000  929.191    0.000 layers.py:62(check)
             2572632872  707.670    0.000  868.286    0.000 layers.py:700(<genexpr>)
               15021006  145.678    0.000  847.508    0.000 level.py:41(notUsed)
               90389456  778.927    0.000  778.927    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7710315021  732.140    0.000  732.140    0.000 layer.py:91(positions)
               90389456  712.248    0.000  712.248    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               90389456  662.511    0.000  662.511    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               90389456  645.681    0.000  645.681    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                6485245  209.124    0.000  603.923    0.000 exploration.py:53(softmaxer)
                9684744   25.407    0.000  600.246    0.000 loss.py:527(forward)
                6457984  234.219    0.000  595.352    0.000 random.py:315(sample)
                9684744   66.643    0.000  574.839    0.000 functional.py:2898(mse_loss)
              632726276  450.971    0.000  560.445    0.000 tensor.py:906(grad)
        6348513044/6348513041  466.486    0.000  543.928    0.000 {built-in method builtins.len}
                3228992  312.878    0.000  538.874    0.000 collector.py:46(collect)
                3228992   90.090    0.000  525.714    0.000 agent.py:277(counterfact_check)
              257047396  357.873    0.000  509.254    0.000 layers.py:113(isDone)
              322619262  333.377    0.000  485.258    0.000 layers.py:48(check)
               90389456  468.935    0.000  468.935    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             5547802630  440.377    0.000  440.377    0.000 {built-in method builtins.hash}
              329569664  259.699    0.000  378.728    0.000 layer.py:126(remove)
               15021006   13.235    0.000  377.839    0.000 level.py:38(elementsIn)
              322619262  253.645    0.000  371.994    0.000 layers.py:23(check)
              158102211  341.326    0.000  341.326    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                9684744  337.073    0.000  337.073    0.000 {built-in method torch._C._nn.mse_loss}
                9685714  313.006    0.000  313.006    0.000 {built-in method max}
               22602944  286.650    0.000  286.650    0.000 {built-in method sum}
                6457986  283.730    0.000  283.730    0.000 {built-in method nonzero}
              401481365  200.604    0.000  279.440    0.000 layer.py:130(add)
                9684744   66.665    0.000  265.000    0.000 __init__.py:28(_make_grads)
               19369488   64.414    0.000  252.409    0.000 profiler.py:615(__enter__)
               45330626   42.990    0.000  247.935    0.000 flatten.py:39(forward)
              338603790  156.361    0.000  242.985    0.000 random.py:250(_randbelow_with_getrandbits)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9515522: <ReTest15_0> in cluster <dcc> Done

Job <ReTest15_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr 14 15:03:59 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr 14 20:44:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr 14 20:44:08 2021
Terminated at Thu Apr 15 20:39:38 2021
Results reported at Thu Apr 15 20:39:38 2021

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

    CPU time :                                   85906.33 sec.
    Max Memory :                                 9409 MB
    Average Memory :                             6219.27 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6975.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86132 sec.
    Turnaround time :                            106539 sec.

The output (if any) is above this job summary.

